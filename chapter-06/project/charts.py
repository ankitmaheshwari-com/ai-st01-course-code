# charts.py
import streamlit as st
import plotly.express as px


def display_charts(df):
    st.subheader("Visualizations")

    tab1, tab2 = st.tabs(["Overview", "Trends"])

    with tab1:
        c1, c2 = st.columns(2)

        with c1:
            st.caption("Revenue by Category")
            fig_bar = px.bar(df, x="Category", y="Revenue", color="Category")
            st.plotly_chart(fig_bar, use_container_width=True)

        with c2:
            st.caption("Revenue by Region")
            fig_pie = px.pie(df, values="Revenue", names="Region", hole=0.4)
            st.plotly_chart(fig_pie, use_container_width=True)

    with tab2:
        st.caption("Sales Over Time")
        df_trend = df.set_index("Date").resample("ME")["Revenue"].sum().reset_index()
        fig_line = px.line(df_trend, x="Date", y="Revenue", markers=True)
        st.plotly_chart(fig_line, use_container_width=True)
