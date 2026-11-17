import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Wildfire_Dataset.csv")

# 1. Convert datetime FIRST so date subtraction works properly
df["datetime"] = pd.to_datetime(df["datetime"])

# 2. Detect whenever the coordinate changes OR the date jumps by more than 1 day
coord_changed = (df["latitude"] != df["latitude"].shift()) | (df["longitude"] != df["longitude"].shift())
date_jumped = (df["datetime"] - df["datetime"].shift()).dt.days != 1

# Every time either happens, a new true event sequence begins
df["sample_id"] = (coord_changed | date_jumped).cumsum()

# Convert target text to binary 1/0
df["wf_bin"] = (df["Wildfire"].str.strip().str.lower() == "yes").astype(int)

# 3. Ensure chronological order inside each event sequence and assign day_idx
df = df.sort_values(["sample_id", "datetime"]).reset_index(drop=True)
df["day_idx"] = df.groupby("sample_id").cumcount()

# 4. Determine target label and anchor_day (first 'Yes' day for positives)
sample_target = df.groupby("sample_id")["wf_bin"].max().rename("Wildfire")

# Find anchor day for positive samples (first 'Yes' day)
first_yes = (
    df[df["wf_bin"] == 1]
    .groupby("sample_id")["day_idx"]
    .min()
    .rename("anchor_day")
)

# For negative samples (target == 0), anchor at day 75 (or the last available day if < 75)
max_day = df.groupby("sample_id")["day_idx"].max().rename("max_day")
meta = pd.concat([sample_target, max_day, first_yes], axis=1).reset_index()
meta["anchor_day"] = meta["anchor_day"].fillna(meta["max_day"]).astype(int)

df = df.merge(meta[["sample_id", "target", "anchor_day"]], on="sample_id", how="left")

# 5. Keep only the 60-day pre-event window up through the anchor day (-59 to 0)
df["rel_day"] = df["day_idx"] - df["anchor_day"]
df_valid = df[(df["rel_day"] >= -59) & (df["rel_day"] <= 0)].copy()

# 6. Snapshot of weather on the exact target day (rel_day == 0)
day0 = (
    df_valid[df_valid["rel_day"] == 0]
    .set_index("sample_id")[["latitude", "longitude", "datetime", "target", 
                             "pr", "rmax", "rmin", "sph", "srad", "tmmn"]]
)

# 7. 7-day antecedent window
last_7d = df_valid[df_valid["rel_day"] >= -6].groupby("sample_id").agg(
    pr_sum_7d=("pr", "sum"),
    rmin_mean_7d=("rmin", "mean"),
    rmax_mean_7d=("rmax", "mean"),
    tmmn_mean_7d=("tmmn", "mean"),
    srad_mean_7d=("srad", "mean"),
)

# 8. 30-day antecedent window
last_30d = df_valid[df_valid["rel_day"] >= -29].groupby("sample_id").agg(
    pr_sum_30d=("pr", "sum"),
    rmin_mean_30d=("rmin", "mean"),
    rmax_mean_30d=("rmax", "mean"),
    tmmn_mean_30d=("tmmn", "mean"),
    sph_mean_30d=("sph", "mean"),
)

# 9. 60-day antecedent window
last_60d = df_valid.groupby("sample_id").agg(
    pr_sum_60d=("pr", "sum"),
    rmin_mean_60d=("rmin", "mean"),
    rmax_mean_60d=("rmax", "mean"),
    tmmn_mean_60d=("tmmn", "mean"),
)

# 10. Days Since Last Rain (DSLR): consecutive dry days (pr < 1.0 mm) before target day
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

# 11. Combine all features into final ABT
abt = pd.concat([day0, last_7d, last_30d, last_60d, dslr], axis=1).reset_index()

# 12. Cap all floating-point columns at 3 decimal places
float_cols = abt.select_dtypes(include=["float", "float32", "float64"]).columns
abt[float_cols] = abt[float_cols].round(3)

abt.to_csv("us_wildfire_abt.csv", index=False)