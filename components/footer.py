"""
====================================================
AI HEALTH GUARDIAN
Professional Footer
Final Version
====================================================
"""

import streamlit as st


def show_footer():
    """
    Displays the application footer.
    """

    st.markdown("---")

    # ==========================================
    # TECHNOLOGY STACK
    # ==========================================

    st.subheader("🚀 Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("☁ IBM watsonx.ai")

    with col2:
        st.success("🧠 Meta Llama 3.3")

    with col3:
        st.success("🤖 Scikit-learn")

    with col4:
        st.success("🎨 Streamlit")

    st.markdown("---")

    # ==========================================
    # PROJECT FEATURES
    # ==========================================

    st.subheader("✨ Project Highlights")

    left, right = st.columns(2)

    with left:

        st.write("✅ Machine Learning Prediction")

        st.write("✅ IBM watsonx.ai")

        st.write("✅ Medical Reasoning Agent")

        st.write("✅ Lifestyle Planning Agent")

        st.write("✅ Reminder Agent")

    with right:

        st.write("✅ AI Health Chat")

        st.write("✅ Patient History")

        st.write("✅ PDF Report")

        st.write("✅ Interactive Dashboard")

        st.write("✅ Agentic AI Workflow")

    st.markdown("---")

    # ==========================================
    # DISCLAIMER
    # ==========================================

    st.warning(
        """
### ⚠ Medical Disclaimer

This application is intended for **educational and decision-support purposes only**.

It is **NOT** a substitute for professional medical advice,
diagnosis or treatment.

Always consult a qualified healthcare professional before
making medical decisions.
"""
    )

    st.markdown("---")

    # ==========================================
    # FOOTER
    # ==========================================

    st.markdown(
        """
<div style="text-align:center;padding:20px;">

<h3 style="color:#0F62FE;">
🏥 AI Health Guardian
</h3>

<p>
Agentic AI for Chronic Disease Monitoring
</p>

<p>
Powered by
<b>IBM watsonx.ai</b> •
<b>Meta Llama 3.3</b> •
<b>Scikit-learn</b> •
<b>Streamlit</b>
</p>

<p style="color:gray;">
Version 2.0
</p>

<p style="color:gray;">
© 2026 AI Health Guardian
</p>

</div>
""",
        unsafe_allow_html=True,
    )