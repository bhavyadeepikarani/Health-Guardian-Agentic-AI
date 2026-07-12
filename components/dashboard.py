"""
====================================================
AI HEALTH GUARDIAN
Professional Dashboard
Final Version
====================================================
"""

import streamlit as st


def show_dashboard():

    # ==========================================
    # HERO SECTION
    # ==========================================

    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg,#0F62FE,#42BE65);
            padding:30px;
            border-radius:20px;
            color:white;
            margin-bottom:20px;
        ">

        <h1 style="color:white;">
        🏥 AI Health Guardian
        </h1>

        <h4 style="color:white;">
        Agentic AI for Chronic Disease Monitoring
        </h4>

        <p>
        Predict diabetes risk using Machine Learning,
        receive AI-powered medical reasoning from IBM watsonx.ai,
        generate lifestyle plans,
        create PDF reports,
        and interact with an intelligent healthcare assistant.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # SYSTEM STATUS
    # ==========================================

    st.subheader("🚀 System Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🤖 AI Agents",
            "8",
            "Active"
        )

    with c2:
        st.metric(
            "🧠 ML Model",
            "Ready"
        )

    with c3:
        st.metric(
            "☁ IBM",
            "Connected"
        )

    with c4:
        st.metric(
            "📄 Reports",
            "Enabled"
        )

    st.markdown("---")

    # ==========================================
    # FEATURES
    # ==========================================

    st.subheader("✨ Key Features")

    f1, f2 = st.columns(2)

    with f1:

        st.success("✔ Diabetes Risk Prediction")

        st.success("✔ IBM watsonx.ai")

        st.success("✔ Meta Llama 3.3")

        st.success("✔ Medical Reasoning")

        st.success("✔ Lifestyle Planning")

    with f2:

        st.success("✔ Reminder Agent")

        st.success("✔ AI Health Chat")

        st.success("✔ PDF Report")

        st.success("✔ Patient History")

        st.success("✔ Interactive Dashboard")

    st.markdown("---")

    # ==========================================
    # HOW IT WORKS
    # ==========================================

    st.subheader("⚙ AI Workflow")

    st.info(
        """
1️⃣ Enter Patient Information

⬇

2️⃣ Machine Learning predicts Diabetes Risk

⬇

3️⃣ IBM watsonx.ai generates Medical Reasoning

⬇

4️⃣ Lifestyle Agent creates a Health Plan

⬇

5️⃣ Reminder Agent prepares Daily Reminders

⬇

6️⃣ PDF Report is Generated

⬇

7️⃣ AI Chat answers Health Questions
"""
    )

    st.markdown("---")


    # ==========================================
    # HEALTH FACTS
    # ==========================================

    st.subheader("🩺 Healthy Lifestyle Tips")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
🥗 Healthy Diet

Eat fruits, vegetables,

whole grains and

avoid sugary drinks.
"""
        )

    with col2:

        st.info(
            """
🏃 Stay Active

Exercise

at least

30 minutes daily.
"""
        )

    with col3:

        st.info(
            """
😴 Good Sleep

Sleep

7–8 hours

every night.
"""
        )

    st.markdown("---")

    # ==========================================
    # START MESSAGE
    # ==========================================

    st.success(
        "👇 Fill in the Patient Information below and click **Analyze Health** to start."
    )