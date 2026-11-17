import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Wildfire_Dataset.csv")

df["sample_id"] = df.index // 75
coord_counts = df.groupby("sample_id")[["latitude", "longitude"]].nunique()
print(coord_counts.max())

df2 = pd.read_csv("us_wildfire_abt.csv")

coord_counts = df2.groupby("sample_id")[["latitude", "longitude"]].nunique()
print(coord_counts.max())