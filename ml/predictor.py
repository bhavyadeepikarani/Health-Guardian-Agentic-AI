import os
import joblib
import numpy as np
import pandas as pd


# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Model paths
model_path = os.path.join(
    BASE_DIR,
    "models",
    "diabetes_model.pkl"
)

scaler_path = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)


# Load model and scaler once
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)


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

    features = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"
    ]

    # Create dataframe to preserve feature names
    sample = pd.DataFrame(
        [data],
        columns=features
    )

    # Scale input
    sample_scaled = scaler.transform(sample)

    # Prediction
    prediction = model.predict(sample_scaled)[0]

    # Probability
    probability = model.predict_proba(sample_scaled)[0][1]

    return prediction, probability