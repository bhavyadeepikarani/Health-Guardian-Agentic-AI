"""
====================================================
AI HEALTH GUARDIAN
Professional Prediction Dashboard
Version 2.0
====================================================
"""

import streamlit as st
import plotly.graph_objects as go


# =====================================================
# Gauge Chart
# =====================================================

def gauge_chart(probability):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            number={
                "suffix": "%",
                "font": {"size": 42}
            },
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#0F62FE"},
                "steps": [
                    {"range": [0, 40], "color": "#42BE65"},
                    {"range": [40, 70], "color": "#F1C21B"},
                    {"range": [70, 100], "color": "#DA1E28"},
                ],
            },
        )
    )

    fig.update_layout(
        height=330,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
    )

    return fig


# =====================================================
# Donut Chart
# =====================================================

def donut_chart(probability):

    risk = probability * 100
    healthy = 100 - risk

    fig = go.Figure(
        go.Pie(
            values=[risk, healthy],
            labels=["Risk", "Healthy"],
            hole=0.68,
            marker=dict(
                colors=[
                    "#DA1E28",
                    "#42BE65"
                ]
            ),
            textinfo="label+percent",
        )
    )

    fig.update_layout(
        height=330,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        legend=dict(
            orientation="h",
            y=-0.15,
            x=0.2
        ),
    )

    return fig


# =====================================================
# Prediction Dashboard
# =====================================================

def show_prediction(prediction, probability, risk):

    st.header("📊 Diabetes Risk Assessment")

    st.caption(
        "Machine Learning prediction based on the patient's clinical parameters."
    )

    st.divider()

    # -------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        if prediction == 1:
            st.error("⚠ Diabetes Risk Detected")
        else:
            st.success("✅ No Diabetes Risk Detected")

    with col2:

        st.metric(
            "Risk Probability",
            f"{probability*100:.2f}%"
        )

    with col3:

        st.metric(
            "Risk Category",
            risk
        )

    st.progress(probability)

    st.caption(
        f"Overall Prediction Confidence : {probability*100:.2f}%"
    )

    st.divider()

    # -------------------------------------------------

    chart1, chart2 = st.columns(2)

    with chart1:

        st.subheader("Risk Gauge")

        st.plotly_chart(
            gauge_chart(probability),
            width="stretch"
        )

    with chart2:

        st.subheader("Risk Distribution")

        st.plotly_chart(
            donut_chart(probability),
            width="stretch"
        )

    st.divider()

    # -------------------------------------------------

    st.subheader("🧠 Clinical Interpretation")

    if risk == "High":

        st.error(
            """
### 🔴 High Risk

The patient's clinical parameters indicate a **high probability of diabetes**.

**Recommended Actions**

- Schedule a physician consultation immediately.
- Monitor blood glucose regularly.
- Reduce sugar intake.
- Begin supervised exercise.
- Follow medical advice and laboratory testing.
"""
        )

    elif risk == "Medium":

        st.warning(
            """
### 🟡 Moderate Risk

The patient shows **moderate diabetes risk**.

**Recommended Actions**

- Improve dietary habits.
- Exercise for at least 30 minutes daily.
- Reduce processed foods.
- Monitor glucose periodically.
- Maintain a healthy body weight.
"""
        )

    else:

        st.success(
            """
### 🟢 Low Risk

Current indicators suggest **low diabetes risk**.

**Recommended Actions**

- Continue a healthy lifestyle.
- Maintain regular physical activity.
- Eat a balanced diet.
- Stay hydrated.
- Undergo routine health screenings.
"""
        )

    st.divider()

    # -------------------------------------------------

    st.subheader("📌 Key Observation")

    observations = [
        f"Prediction Confidence : **{probability*100:.2f}%**",
        f"Risk Category : **{risk}**",
        "Prediction generated using the trained Machine Learning model.",
        "Further AI reasoning and lifestyle planning are available in the next tab.",
    ]

    for item in observations:
        st.write(f"✔ {item}")