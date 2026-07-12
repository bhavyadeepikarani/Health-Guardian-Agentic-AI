print("Starting test...")

from utils.ibm_connection import ask_llama

print("Imported successfully.")

prompt = """
A 40-year-old patient has:
- Glucose: 160
- BMI: 32
- Diabetes Risk: High (65%)

Explain the result in simple language and give 5 lifestyle recommendations.
"""

print("Sending prompt...")

response = ask_llama(prompt)

print("Response received:")
print(response)