from utils.ibm_connection import ask_llama

def generate_lifestyle_plan(patient_data, risk):

    prompt = f"""
You are a certified nutritionist and fitness coach.

Patient Information:
{patient_data}

Risk Level:
{risk}

Create a personalized health plan.

Include:

1. 7-day diet plan
2. Exercise plan
3. Water intake
4. Sleep schedule
5. Foods to avoid
6. Stress management

Use headings and bullet points.
"""
    return ask_llama(prompt)