from ml.predictor import predict_diabetes

patient = [
    2,
    140,
    75,
    25,
    100,
    31.2,
    0.55,
    40
]

prediction, probability = predict_diabetes(patient)

print("Prediction:", prediction)
print("Probability:", probability)