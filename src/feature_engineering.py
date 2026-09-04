import pandas as pd

df = pd.read_csv("data/cars_cleaned.csv")
df['car_age'] = 2026 - df['year']
df['engine_volume_liters'] = df['engine_volume_cm3'] / 1000
df.to_csv("data/cars_featured.csv", index=False)
print("inženjering završen.")