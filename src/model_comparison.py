import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/cars_featured.csv")
X = df[['year', 'mileage', 'engine_volume_liters', 'car_age']].fillna(0)
y = df['priceUSD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=20, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("srednja apsolutna greška (mae):", round(mean_absolute_error(y_test, preds), 2))

# ovo automatski snima model u folder models
joblib.dump(model, "models/car_price_model.joblib")
print("model uspješno sačuvan u models/car_price_model.joblib")