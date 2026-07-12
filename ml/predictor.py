import joblib
import numpy as np

# Load model and scaler once
model = joblib.load("models/diabetes_model.pkl")
scaler = joblib.load("models/scaler.pkl")


def predict_diabetes(data):
    """
    data = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]
    """

    sample = np.array(data).reshape(1, -1)

    sample = scaler.transform(sample)

    prediction = model.predict(sample)[0]

    probability = model.predict_proba(sample)[0][1]

    return prediction, probability