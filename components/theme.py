"""
====================================================
AI HEALTH GUARDIAN
Theme Configuration
Loads CSS from assets/styles.css
====================================================
"""

import streamlit as st
import os


def load_theme():
    """
    Loads the application's custom CSS theme.
    """

    css_path = os.path.join("assets", "styles.css")

    try:
        with open(css_path, "r", encoding="utf-8") as css_file:
            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:
        st.warning(
            f"CSS file not found: {css_path}"
        )