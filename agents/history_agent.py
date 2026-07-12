"""
====================================================
AI HEALTH GUARDIAN
History Agent
Updated Version
====================================================
"""

import os
import pandas as pd

FILE_PATH = "data/patient_history.csv"


def save_history(patient_data, probability, risk):
    """
    Save patient history to CSV.
    """

    # -------------------------------------------------
    # Convert dictionary to readable text
    # -------------------------------------------------

    if isinstance(patient_data, dict):
        patient_text = " | ".join(
            f"{key}: {value}"
            for key, value in patient_data.items()
        )
    else:
        patient_text = str(patient_data).replace("\n", " | ")

    # -------------------------------------------------
    # Create Record
    # -------------------------------------------------

    record = {
        "Patient": patient_text,
        "Probability": round(probability * 100, 2),
        "Risk": risk
    }

    new_df = pd.DataFrame([record])

    # -------------------------------------------------
    # Append Existing Records
    # -------------------------------------------------

    if os.path.exists(FILE_PATH):

        if os.path.getsize(FILE_PATH) > 0:

            old_df = pd.read_csv(FILE_PATH)

            new_df = pd.concat(
                [old_df, new_df],
                ignore_index=True
            )

    # -------------------------------------------------
    # Save CSV
    # -------------------------------------------------

    os.makedirs("data", exist_ok=True)

    new_df.to_csv(
        FILE_PATH,
        index=False
    )


def load_history():
    """
    Load patient history from CSV.
    """

    if (
        os.path.exists(FILE_PATH)
        and os.path.getsize(FILE_PATH) > 0
    ):
        return pd.read_csv(FILE_PATH)

    return pd.DataFrame()