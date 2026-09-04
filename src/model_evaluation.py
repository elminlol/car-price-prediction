import pandas as pd

df = pd.read_csv("data/cars_featured.csv")
print("ukupno redova u datasetu:", len(df))
print("prosječna cijena automobila:", round(df['priceUSD'].mean(), 2), "dolara")