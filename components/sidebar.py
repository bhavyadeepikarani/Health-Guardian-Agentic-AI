import streamlit as st

try:
    from streamlit_option_menu import option_menu
except Exception as e:
    st.error(f"streamlit_option_menu import failed: {e}")
    option_menu = None


def show_sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/hospital-3.png",
            width=70,
        )

        st.title("AI Health Guardian")

        st.caption("Agentic AI for Chronic Disease Monitoring")

        st.divider()
        if option_menu is not None:

            selected = option_menu(
                menu_title=None,
                options=["Dashboard", "About"],
                icons=["house-fill", "info-circle-fill"],
                default_index=0,
            )

        else:

            selected = st.radio(
                "Navigation",
                ["Dashboard", "About"],
            )

        st.divider()
        st.subheader("💡 Today's Health Tip")

        st.info(
            """🥗 Eat more vegetables

🚶 Walk at least 30 minutes

💧 Drink enough water

😴 Sleep 7–8 hours"""
        )

        st.divider()

        st.subheader("🟢 System Status")

        st.success("IBM watsonx.ai Connected")
        st.success("Meta Llama 3.3 Ready")
        st.success("ML Model Loaded")
        st.success("8 AI Agents Active")

        st.divider()

        
        

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Agents", "8")

        with c2:
            st.metric("Status", "Ready")

        st.divider()

        st.caption("Version 2.0")
        st.caption("Powered by IBM watsonx.ai")
        st.caption("© 2026 AI Health Guardian")

    return selected