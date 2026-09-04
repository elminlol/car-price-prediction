import pandas as pd

df = pd.read_csv("data/cars.csv")
df = df.rename(columns={'mileage(kilometers)': 'mileage', 'volume(cm3)': 'engine_volume_cm3'})
df = df[df['priceUSD'] > 500]
df.to_csv("data/cars_cleaned.csv", index=False)
print("čišćenje završeno.")