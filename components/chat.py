"""
====================================================
AI HEALTH GUARDIAN
AI Chat Component
Final Version
====================================================
"""

import streamlit as st
from agents.chat_agent import chat_with_patient


def show_chat(patient_data):
    """
    Displays a ChatGPT-style AI Health Assistant.

    Parameters
    ----------
    patient_data : str
        Patient information used as context
        for the AI model.
    """

    st.header("💬 AI Health Assistant")

    st.caption(
        "Ask health-related questions about the patient's report."
    )

    st.markdown("---")

    # ==================================================
    # SESSION STATE
    # ==================================================

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ==================================================
    # DISPLAY CHAT HISTORY
    # ==================================================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # ==================================================
    # CHAT INPUT
    # ==================================================

    prompt = st.chat_input(
        "Ask something about the patient's health..."
    )

    if prompt:

        # -----------------------------
        # USER MESSAGE
        # -----------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        # -----------------------------
        # AI RESPONSE
        # -----------------------------

        with st.chat_message("assistant"):

            with st.spinner("🤖 IBM watsonx.ai is thinking..."):

                answer = chat_with_patient(
                    patient_data,
                    prompt
                )

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    st.markdown("---")

    # ==================================================
    # CLEAR CHAT
    # ==================================================

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    # ==================================================
    # SAMPLE QUESTIONS
    # ==================================================

    st.subheader("💡 Try Asking")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
• Can I eat rice?

• Is my glucose level high?

• What foods should I avoid?

• Is my BMI normal?
""")

    with col2:

        st.info("""
• Which exercise is best?

• Can diabetes be prevented?

• Should I consult a doctor?

• How can I reduce my risk?
""")

    st.markdown("---")

    st.success(
        "Your conversation remains available until you refresh or restart the app."
    )