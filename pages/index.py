import streamlit as st

st.title("🫀 Heart Attack Prediction", text_alignment="center", anchor=False)

st.subheader("Estimate heart attack risk using health indicators, lifestyle and machine learning", anchor=False)

st.warning(
    "This tool is for educational purposes only and does not provide medical diagnosis."
)

st.markdown("### What does this app do?\nThis application predicts heart attack risk based on basic health and lifestyle data. It is designed to increase awareness and encourage preventive care.")

st.markdown("### How it works\n1. Enter your health and lifestyle data\n2. Click **Submit**\n3. View your estimated risk level")

if st.button("Start Risk Assessment", width="stretch"):
    st.switch_page("pages/predict_new_model.py")