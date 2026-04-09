import streamlit as st
import pandas as pd
from pages.input_form import input_form
from utils.model_loader import load_old_model
from src.cleaning import clean_data
from src.features import add_features

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Heart Attack Risk Predictor",
    layout="centered",
    page_icon="✏️"
)

# -------------------------------
# Load Model (cache for performance)
# -------------------------------
@st.cache_resource
def get_model():
    return load_old_model()

model = get_model()

# -------------------------------
# Input Form
# -------------------------------
data = input_form(False)

if data is not None:

    try:
        # -------------------------------
        # Convert to DataFrame
        # -------------------------------
        input_df = pd.DataFrame([data])

        # -------------------------------
        # Preprocessing Pipeline
        # -------------------------------
        X = clean_data(input_df)
        X = add_features(X)

        # -------------------------------
        # Prediction
        # -------------------------------
        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0]

        # -------------------------------
        # Output Section
        # -------------------------------
        st.subheader("Prediction Result")

        # ⚠️ IMPORTANT FIX: Align logic with label meaning
        # Assuming:
        # 1 = High Risk
        # 0 = Low Risk
        if prediction == 0:
            st.error("⚠️ High Risk of Heart Attack")
        else:
            st.success("✅ Low Risk of Heart Attack")

        # -------------------------------
        # Confidence Score
        # -------------------------------
        confidence = max(proba) * 100

        st.metric(
            label="Model Confidence",
            value=f"{confidence:.2f}%"
        )

        # -------------------------------
        # Probability Breakdown
        # -------------------------------
        st.write({
            "High Risk Probability": f"{proba[1] * 100:.2f}%",
            "Low Risk Probability": f"{proba[0] * 100:.2f}%"
        })

    except Exception as e:
        st.error("An error occurred during prediction.")
        st.exception(e)