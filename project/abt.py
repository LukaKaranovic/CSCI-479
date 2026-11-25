import pandas as pd

# Load dataset
df = pd.read_csv("Wildfire_Dataset.csv")

# Convert datetime FIRST so date subtraction works properly
df["datetime"] = pd.to_datetime(df["datetime"])

# Detect whenever the coordinate changes OR the date jumps by more than 1 day
coord_changed = (df["latitude"] != df["latitude"].shift()) | (df["longitude"] != df["longitude"].shift())
date_jumped = (df["datetime"] - df["datetime"].shift()).dt.days != 1

# Every time either happens, a new true event sequence begins
df["sample_id"] = (coord_changed | date_jumped).cumsum()

# Convert target attribute text to binary 1/0
df["wf_bin"] = (df["Wildfire"].str.strip().str.lower() == "yes").astype(int)

# Ensure chronological order inside each event sequence and assign day_idx
df = df.sort_values(["sample_id", "datetime"]).reset_index(drop=True)
df["day_idx"] = df.groupby("sample_id").cumcount()

# Determine target attribute label and anchor_day (first 'Yes' day for positives)
sample_target = df.groupby("sample_id")["wf_bin"].max().rename("Wildfire")

# Find anchor day for positive samples (first 'Yes' day)
first_yes = (
    df[df["wf_bin"] == 1]
    .groupby("sample_id")["day_idx"]
    .min()
    .rename("anchor_day")
)

# For negative samples (Wildfire == 0), anchor at day 75 (or the last available day if < 75)
max_day = df.groupby("sample_id")["day_idx"].max().rename("max_day")
meta = pd.concat([sample_target, max_day, first_yes], axis=1).reset_index()
meta["anchor_day"] = meta["anchor_day"].fillna(meta["max_day"]).astype(int)

df = df.merge(meta[["sample_id", "Wildfire", "anchor_day"]], on="sample_id", how="left")

# Keep only the 60-day pre-event window up through the anchor day (-59 to 0)
df["rel_day"] = df["day_idx"] - df["anchor_day"]
df_valid = df[(df["rel_day"] >= -59) & (df["rel_day"] <= 0)].copy()

# Snapshot of weather on the exact day of wildfire (rel_day == 0)
day0 = (
    df_valid[df_valid["rel_day"] == 0]
    .set_index("sample_id")[["latitude", "longitude", "datetime", 
                             "pr", "rmax", "rmin", "sph", "srad", "tmmn"]]
)

# 7-day antecedent window
last_7d = df_valid[df_valid["rel_day"] >= -6].groupby("sample_id").agg(
    pr_sum_7d=("pr", "sum"),
    rmin_mean_7d=("rmin", "mean"),
    rmax_mean_7d=("rmax", "mean"),
    tmmn_mean_7d=("tmmn", "mean"),
    srad_mean_7d=("srad", "mean"),
)

# 30-day antecedent window
last_30d = df_valid[df_valid["rel_day"] >= -29].groupby("sample_id").agg(
    pr_sum_30d=("pr", "sum"),
    rmin_mean_30d=("rmin", "mean"),
    rmax_mean_30d=("rmax", "mean"),
    tmmn_mean_30d=("tmmn", "mean"),
    sph_mean_30d=("sph", "mean"),
)

# 60-day antecedent window
last_60d = df_valid.groupby("sample_id").agg(
    pr_sum_60d=("pr", "sum"),
    rmin_mean_60d=("rmin", "mean"),
    rmax_mean_60d=("rmax", "mean"),
    tmmn_mean_60d=("tmmn", "mean"),
)

# Days Since Last Rain (DSLR): consecutive dry days (pr < 1.0 mm) before day of wildfire.
def calc_dslr(group):
    rain = group.sort_values("rel_day", ascending=False)["pr"].values
    dry_days = 0
    for r in rain:
        if r < 1.0:
            dry_days += 1
        else:
            break
    return dry_days

dslr = df_valid.groupby("sample_id").apply(calc_dslr).rename("days_since_last_rain")

# Combine all features into final ABT
abt = pd.concat([day0, last_7d, last_30d, last_60d, dslr, sample_target], axis=1).reset_index()


# Cap all floating-point columns at 3 decimal places
float_cols = abt.select_dtypes(include=["float", "float32", "float64"]).columns
abt[float_cols] = abt[float_cols].round(3)

# -- SPLIT INTO TRAINING AND VALIDATION DATASETS --


# Ensure datetime is parsed as a datetime object
abt["datetime"] = pd.to_datetime(abt["datetime"])

# Save original .csv
abt.to_csv("us_wildfire_abt.csv", index=False)

# Temporal split: Pre-2022 for training, 2022–2023 for validation
train_df = abt[abt["datetime"].dt.year < 2022].copy()
val_df = abt[abt["datetime"].dt.year >= 2022].copy()

# Check split sizes and class distribution
print(f"Training set:   {len(train_df):,} rows ({len(train_df)/len(abt):.1%})")
print(train_df["Wildfire"].value_counts(normalize=True).round(3))

print(f"\nValidation set: {len(val_df):,} rows ({len(val_df)/len(abt):.1%})")
print(val_df["Wildfire"].value_counts(normalize=True).round(3))

# Export to separate CSV files
train_df.to_csv("us_wildfire_train.csv", index=False)
val_df.to_csv("us_wildfire_val.csv", index=False)
