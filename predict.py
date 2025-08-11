import joblib
import pandas as pd

def predict_yield(input_data):
    model = joblib.load("results/crop_yield_model.pkl")
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return prediction

if __name__ == "__main__":
    sample_input = {
        "N": 90,
        "P": 40,
        "K": 40,
        "temperature": 25,
        "humidity": 80,
        "ph": 6.5,
        "rainfall": 200
    }
    result = predict_yield(sample_input)
    print(f"Predicted Crop Yield: {result:.2f} kg/ha")
