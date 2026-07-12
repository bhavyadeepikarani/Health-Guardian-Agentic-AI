from ml.predictor import predict_diabetes


def analyze_patient(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    diabetes_pedigree,
    age
):
    patient = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]

    prediction, probability = predict_diabetes(patient)

    if probability < 0.30:
        risk = "Low"
    elif probability < 0.70:
        risk = "Medium"
    else:
        risk = "High"

    return prediction, probability, risk