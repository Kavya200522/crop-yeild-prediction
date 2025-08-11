import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from preprocess import load_and_preprocess_data

X_train, X_test, y_train, y_test = load_and_preprocess_data("data/100.csv")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
joblib.dump(model, "results/crop_yield_model.pkl")
