# ============================================================
# AI HEALTH GUARDIAN
# Agentic AI for Chronic Disease Monitoring
# Final Version 2.0
# ============================================================

# ============================================================
# IMPORT LIBRARIES
# ============================================================

import streamlit as st
from streamlit_lottie import st_lottie
from utils.lottie_loader import load_lottie
# ---------- Agents ----------
from agents.health_agent import analyze_patient
from agents.medical_agent import generate_medical_reasoning
from agents.lifestyle_agent import generate_lifestyle_plan
from agents.reminder_agent import generate_reminders
from agents.history_agent import save_history, load_history
from agents.chat_agent import chat_with_patient

# ---------- Utilities ----------
from utils.pdf_generator import create_pdf

# ---------- Components ----------
from components.theme import load_theme
from components.sidebar import show_sidebar
from components.dashboard import show_dashboard
from components.patient_form import show_patient_form
from components.prediction import show_prediction
from components.analysis import show_analysis
from components.reports import show_reports
from components.history import show_history
from components.chat import show_chat
from components.footer import show_footer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Health Guardian",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD CUSTOM CSS
# ============================================================

#load_theme()
loading_animation = load_lottie("assets/animations.json")


# ============================================================
# INITIALIZE SESSION STATE
# ============================================================

if "analysis_completed" not in st.session_state:
    st.session_state.analysis_completed = False

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "probability" not in st.session_state:
    st.session_state.probability = None

if "risk" not in st.session_state:
    st.session_state.risk = None

if "patient_data" not in st.session_state:
    st.session_state.patient_data = ""

if "medical_reasoning" not in st.session_state:
    st.session_state.medical_reasoning = ""

if "lifestyle" not in st.session_state:
    st.session_state.lifestyle = ""

if "reminders" not in st.session_state:
    st.session_state.reminders = []

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = ""


# ============================================================
# SIDEBAR
# ============================================================

selected_page = show_sidebar()


# ============================================================
# ABOUT PAGE
# ============================================================

if selected_page == "About":

    st.title("🏥 AI Health Guardian")

    st.markdown("""
### Agentic AI for Chronic Disease Monitoring

AI Health Guardian is an intelligent healthcare assistant that combines
Machine Learning with IBM watsonx.ai to predict diabetes risk and provide
personalized recommendations.

---

### 🚀 Features

- Diabetes Risk Prediction
- IBM watsonx.ai Integration
- Meta Llama 3.3
- Medical Reasoning Agent
- Lifestyle Planning Agent
- Reminder Agent
- PDF Report Generator
- Patient History
- AI Health Chat

---

### 👩‍💻 Technology Stack

- IBM watsonx.ai Runtime
- Meta Llama 3.3 70B
- Scikit-learn
- Streamlit
- Plotly
- Pandas

---

Developed as an Agentic AI Healthcare Solution.
""")

    show_footer()

    st.stop()


# ============================================================
# DASHBOARD
# ============================================================

show_dashboard()


# ============================================================
# PATIENT FORM
# ============================================================

analyze, patient = show_patient_form()


# ============================================================
# START ANALYSIS
# ============================================================

if analyze:

    with st.spinner("🔍 Predicting diabetes risk..."):

        prediction, probability, risk = analyze_patient(
            patient["pregnancies"],
            patient["glucose"],
            patient["blood_pressure"],
            patient["skin_thickness"],
            patient["insulin"],
            patient["bmi"],
            patient["diabetes_pedigree"],
            patient["age"]
        )

    patient_data = {
    "Age": patient["age"],
    "Pregnancies": patient["pregnancies"],
    "Glucose": patient["glucose"],
    "Blood Pressure": patient["blood_pressure"],
    "Skin Thickness": patient["skin_thickness"],
    "Insulin": patient["insulin"],
    "BMI": patient["bmi"],
    "Diabetes Pedigree": patient["diabetes_pedigree"],
}
    # Text (used for IBM AI)
    patient_text = f"""
    Age: {patient["age"]}
    Pregnancies: {patient["pregnancies"]}
    Glucose: {patient["glucose"]}
    Blood Pressure: {patient["blood_pressure"]}
    Skin Thickness: {patient["skin_thickness"]}
    Insulin: {patient["insulin"]}
    BMI: {patient["bmi"]}
    Diabetes Pedigree: {patient["diabetes_pedigree"]}
    """
        # ============================================================
    # SAVE PATIENT HISTORY
    # ============================================================

    save_history(
        patient_data,
        probability,
        risk
    )

    # ============================================================
    # MEDICAL REASONING AGENT
    # ============================================================

    
    medical_placeholder = st.empty()

    medical_placeholder.info("🧠 AI Medical Agent is analyzing...")

    with medical_placeholder.container():
        st_lottie(
        loading_animation,
        height=180,
        key="medical_animation"
    )

    medical_reasoning = generate_medical_reasoning(
        patient_text,
        probability,
        risk
    )

    medical_placeholder.empty()

    # ============================================================
    # LIFESTYLE PLANNING AGENT
    # ============================================================

    lifestyle_placeholder = st.empty()

    lifestyle_placeholder.info("🥗 Preparing your personalized lifestyle plan...")

    with lifestyle_placeholder.container():
        st_lottie(
        loading_animation,
        height=180,
        key="lifestyle_animation"
    )

    lifestyle = generate_lifestyle_plan(
        patient_text,
        risk
    )

    lifestyle_placeholder.empty()

    # ============================================================
    # REMINDER AGENT
    # ============================================================

    reminders = generate_reminders(
        risk
    )

    # ============================================================
    # PDF REPORT GENERATION
    # ============================================================

    combined_report = f"""
==========================
AI HEALTH REPORT
==========================

MEDICAL REASONING

{medical_reasoning}

==================================================

PERSONALIZED LIFESTYLE PLAN

{lifestyle}
"""

    pdf_path = create_pdf(
        patient_text,
        probability,
        risk,
        combined_report,
        reminders
    )

    # ============================================================
    # STORE EVERYTHING IN SESSION STATE
    # ============================================================

    st.session_state.analysis_completed = True

    st.session_state.prediction = prediction

    st.session_state.probability = probability

    st.session_state.risk = risk

    st.session_state.patient_data = patient_data

    st.session_state.medical_reasoning = medical_reasoning
    st.session_state.lifestyle = lifestyle

    st.session_state.reminders = reminders

    st.session_state.pdf_path = pdf_path


# ============================================================
# DISPLAY RESULTS
# ============================================================

if st.session_state.analysis_completed:

    st.markdown("---")

    st.header("📊 AI Analysis Results")

    # ============================================================
    # RESULT TABS
    # ============================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Prediction",
            "🧠 AI Analysis",
            "📄 Reports",
            "📚 History",
            "💬 AI Chat"
        ]
    )
        # ============================================================
    # TAB 1 : PREDICTION DASHBOARD
    # ============================================================

    with tab1:

        show_prediction(
            st.session_state.prediction,
            st.session_state.probability,
            st.session_state.risk
        )

    # ============================================================
    # TAB 2 : AI ANALYSIS
    # ============================================================

    with tab2:

        show_analysis(
            st.session_state.medical_reasoning,
            st.session_state.lifestyle,
            st.session_state.reminders
        )

    # ============================================================
    # TAB 3 : REPORT CENTER
    # ============================================================

    with tab3:

        show_reports(
            st.session_state.patient_data,
            st.session_state.probability,
            st.session_state.risk,
            st.session_state.pdf_path
        )

    # ============================================================
    # TAB 4 : PATIENT HISTORY
    # ============================================================

    with tab4:

        history = load_history()

        show_history(history)

    # ============================================================
    # TAB 5 : AI HEALTH CHAT
    # ============================================================

    with tab5:

        show_chat(
            st.session_state.patient_data
        )

    # ============================================================
    # ANALYSIS SUMMARY
    # ============================================================

    st.markdown("---")

    st.success("✅ AI Health Analysis Completed Successfully")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Prediction",
            "Completed"
        )

    with c2:
        st.metric(
            "AI Agents",
            "8 Active"
        )

    with c3:
        st.metric(
            "Risk Level",
            st.session_state.risk
        )

    with c4:
        st.metric(
            "PDF Report",
            "Generated"
        )

    st.markdown("---")
    # ============================================================
# FOOTER
# ============================================================

show_footer()


# ============================================================
# END OF APPLICATION
# ============================================================

st.markdown("---")

st.caption(
    """
🏥 **AI Health Guardian v2.0**

Built using **IBM watsonx.ai**, **Meta Llama 3.3**, **Scikit-learn**, **Plotly**, and **Streamlit**.

This project demonstrates an **Agentic AI approach** for chronic disease monitoring by integrating machine learning, large language models, intelligent health recommendations, PDF report generation, patient history tracking, and an interactive AI health assistant.

**© 2026 AI Health Guardian • All Rights Reserved**
"""
)

# ============================================================
# OPTIONAL SIDEBAR FOOTER
# ============================================================

with st.sidebar:

    st.markdown("---")

    st.caption("🏥 AI Health Guardian")

    st.caption("Version 2.0")

    st.caption("Powered by IBM watsonx.ai")

    st.caption("Meta Llama 3.3")

    st.caption("Made with ❤️ using Streamlit")