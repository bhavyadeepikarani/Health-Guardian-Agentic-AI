"""
====================================================
AI HEALTH GUARDIAN
Professional Report Center
Version 2.0
====================================================
"""

import os
from datetime import datetime

import pandas as pd
import streamlit as st


def show_reports(
    patient_data,
    probability,
    risk,
    pdf_path,
):
    """
    Displays the complete report center.
    """

    st.header("📄 Report Center")

    st.caption(
        "Download and review the AI-generated patient report."
    )

    st.divider()

    # =====================================================
    # REPORT SUMMARY
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        st.subheader("🩺 Patient Information")

        df = pd.DataFrame(
            patient_data.items(),
            columns=["Parameter", "Value"]
        )

        st.dataframe(
            df,
            width="stretch",
            hide_index=True,
        )

    with right:

        st.subheader("📊 Prediction Summary")

        st.metric(
            "Risk Probability",
            f"{probability*100:.2f}%"
        )

        st.metric(
            "Risk Level",
            risk
        )

        if risk == "High":
            st.error("🔴 High Risk")

        elif risk == "Medium":
            st.warning("🟡 Medium Risk")

        else:
            st.success("🟢 Low Risk")

        st.info(
            f"""
**Generated**

📅 {datetime.now():%d %B %Y}

🕒 {datetime.now():%I:%M %p}
"""
        )

    st.divider()

    # =====================================================
    # PDF DOWNLOAD
    # =====================================================

    st.subheader("📥 Download Report")

    if pdf_path and os.path.exists(pdf_path):

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                label="📄 Download AI Health Report",
                data=pdf,
                file_name="AI_Health_Guardian_Report.pdf",
                mime="application/pdf",
                width="stretch",
            )

        st.success("✅ PDF report is ready.")

    else:

        st.error("PDF report could not be found.")

    st.divider()

    # =====================================================
    # REPORT CONTENTS
    # =====================================================

    st.subheader("📋 Report Contents")

    c1, c2 = st.columns(2)

    with c1:

        st.success("✔ Patient Information")
        st.success("✔ Machine Learning Prediction")
        st.success("✔ Risk Probability")
        st.success("✔ Diabetes Assessment")
        st.success("✔ AI Medical Reasoning")

    with c2:

        st.success("✔ Personalized Lifestyle Plan")
        st.success("✔ Daily Health Reminders")
        st.success("✔ AI Recommendations")
        st.success("✔ Health Summary")
        st.success("✔ Professional PDF Report")

    st.divider()

    # =====================================================
    # REPORT STATUS
    # =====================================================

    st.subheader("📌 Report Status")

    st.info(
        """
The report has been generated successfully.

You may:

• Download the PDF.

• Share it with your physician.

• Store it for future comparison.

• Keep it as part of your health records.
"""
    )

    st.divider()

    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.warning(
        """
### ⚠ Medical Disclaimer

This report is generated using Machine Learning and IBM watsonx.ai.

It is intended for educational and decision-support purposes only.

It should not replace professional medical diagnosis or treatment.

Always consult a qualified healthcare professional before making medical decisions.
"""
    )

    st.divider()

    st.caption(
        "🏥 AI Health Guardian • Powered by IBM watsonx.ai • Meta Llama 3.3 • Scikit-learn • Streamlit"
    )