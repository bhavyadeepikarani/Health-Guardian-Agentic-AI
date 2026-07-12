"""
====================================================
AI HEALTH GUARDIAN
Patient Form Component
Final Version
====================================================
"""

import streamlit as st


def show_patient_form():
    """
    Displays the patient information form.

    Returns
    -------
    patient : dict
        Dictionary containing all patient details.
    """

    st.header("🩺 Patient Information")

    st.caption(
        "Enter the patient's health information to begin the AI-powered analysis."
    )

    st.markdown("---")

    # ====================================================
    # FORM
    # ====================================================

    with st.form("patient_form", clear_on_submit=False):

        col1, col2 = st.columns(2)

        with col1:

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=120,
                value=30,
                step=1,
            )

            glucose = st.number_input(
                "Glucose Level",
                min_value=0,
                value=100,
                step=1,
            )

            blood_pressure = st.number_input(
                "Blood Pressure",
                min_value=0,
                value=80,
                step=1,
            )

            bmi = st.number_input(
                "BMI",
                min_value=0.0,
                value=25.0,
                step=0.1,
            )

        with col2:

            pregnancies = st.number_input(
                "Pregnancies",
                min_value=0,
                value=0,
                step=1,
            )

            insulin = st.number_input(
                "Insulin",
                min_value=0,
                value=80,
                step=1,
            )

            skin_thickness = st.number_input(
                "Skin Thickness",
                min_value=0,
                value=20,
                step=1,
            )

            diabetes_pedigree = st.number_input(
                "Diabetes Pedigree Function",
                min_value=0.0,
                value=0.50,
                step=0.01,
                format="%.2f",
            )

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        with c1:
            analyze = st.form_submit_button(
                "🔍 Analyze Health",
                use_container_width=True,
            )

        with c2:
            sample = st.form_submit_button(
                "🧪 Load Sample",
                use_container_width=True,
            )

        with c3:
            reset = st.form_submit_button(
                "♻ Reset",
                use_container_width=True,
            )

    # ====================================================
    # SAMPLE DATA
    # ====================================================

    if sample:

        age = 45
        glucose = 165
        blood_pressure = 82
        bmi = 31.2
        pregnancies = 2
        insulin = 120
        skin_thickness = 28
        diabetes_pedigree = 0.68

        st.success("Sample patient loaded successfully.")

        analyze = True

    # ====================================================
    # RESET
    # ====================================================

    if reset:

        st.rerun()

    # ====================================================
    # PATIENT DICTIONARY
    # ====================================================

    patient = {
        "age": age,
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": diabetes_pedigree,
    }

    return analyze, patient