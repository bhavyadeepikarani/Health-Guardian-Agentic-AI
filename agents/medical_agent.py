from utils.ibm_connection import ask_llama

def generate_medical_reasoning(patient_data, probability, risk):

    prompt = f"""
You are an experienced doctor.

Patient Details:
{patient_data}

Predicted Diabetes Probability: {probability*100:.2f}%
Risk Level: {risk}

Explain:

1. What the prediction means.
2. Why the patient received this risk.
3. Which health parameters are concerning.
4. Keep the explanation under 200 words.
5. Do NOT provide diet or exercise advice.
"""

    return ask_llama(prompt)