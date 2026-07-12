"""
====================================================
AI HEALTH GUARDIAN
Patient History Component
Updated Version
====================================================
"""

import streamlit as st
import pandas as pd


def show_history(history_df):
    """
    Displays patient history with search,
    filtering and statistics.
    """

    st.header("📚 Patient History")

    st.caption(
        "View previously analyzed patient records."
    )

    st.divider()

    # =====================================================
    # EMPTY HISTORY
    # =====================================================

    if history_df is None or history_df.empty:
        st.info("No patient history available.")
        return

    # =====================================================
    # SEARCH + FILTER
    # =====================================================

    col1, col2 = st.columns([2, 1])

    with col1:
        search = st.text_input(
            "🔍 Search Patient Records"
        )

    with col2:
        selected_risk = st.selectbox(
            "Risk Level",
            ["All", "Low", "Medium", "High"]
        )

    filtered = history_df.copy()

    # =====================================================
    # SEARCH
    # =====================================================

    if search.strip():

        filtered = filtered[
            filtered.astype(str)
            .apply(
                lambda row: row.str.contains(
                    search,
                    case=False,
                    na=False
                ).any(),
                axis=1
            )
        ]

    # =====================================================
    # FILTER
    # =====================================================

    if selected_risk != "All" and "Risk" in filtered.columns:

        filtered = filtered[
            filtered["Risk"] == selected_risk
        ]

    # =====================================================
    # STATISTICS
    # =====================================================

    st.subheader("📊 Statistics")

    total = len(filtered)

    low = medium = high = 0

    if "Risk" in filtered.columns:

        low = (filtered["Risk"] == "Low").sum()
        medium = (filtered["Risk"] == "Medium").sum()
        high = (filtered["Risk"] == "High").sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Records", total)
    c2.metric("Low Risk", low)
    c3.metric("Medium Risk", medium)
    c4.metric("High Risk", high)

    st.divider()

    # =====================================================
    # TABLE
    # =====================================================

    st.subheader("📋 Patient Records")

    st.dataframe(
        filtered,
        width="stretch",
        hide_index=True
    )

    st.divider()

    # =====================================================
    # DOWNLOAD CSV
    # =====================================================

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download History (CSV)",
        data=csv,
        file_name="patient_history.csv",
        mime="text/csv",
        width="stretch"
    )

    st.divider()

    # =====================================================
    # SUMMARY
    # =====================================================

    st.success(
        f"Displaying {len(filtered)} patient record(s)."
    )