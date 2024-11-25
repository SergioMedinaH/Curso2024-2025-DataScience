import pandas as pd

df = pd.read_csv("con_open.csv", index_col=0)
df_copy = df[-df["HousesSold"].isna()]
df_copy.to_csv("housing_london_extra_clean.csv")
