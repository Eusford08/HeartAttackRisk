import streamlit as st

st.set_page_config(page_title="Model Information", layout="centered",page_icon="🧠")

st.title("📊 Model & Dataset Information", anchor=False)

st.markdown(
    """
    This page provides transparency about the machine learning model,
    training data, and evaluation metrics used in this application.
    """
)

st.divider()

st.header("🧠 Model Overview")

st.markdown(
    """
    - **Model Type:** Logistic Regression  
    - **Task:** Binary Classification (Heart Attack Risk: Yes / No)  

    - **Rationale for Selection:**  
      - **High Interpretability:** Coefficients provide clear insight into feature impact, which is critical in medical decision-making  
      - **Clinically Appropriate:** Widely used baseline model for risk prediction in healthcare settings  
      - **Robust on Structured Data:** Performs reliably on tabular datasets with well-defined features  
      - **Low Risk of Overfitting:** Compared to complex models, it generalizes better on smaller or moderate-sized datasets  
    """
)

st.header("📁 Dataset Information")

st.markdown(
    """
    - **Source:** https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset  
    - **Number of Samples:** ~8763 records  
    - **Target Variable:** Heart attack Risk  
    - **Features Include:**  
        - Age  
        - Sex
        - Cholesterol  
        - Heart Rate
        - Diabetes
        - Family History
        - Smoking
        - Obesity
        - Alcohol Consumption
        - Exercise Hours Per Week
        - Diet
        - Previouse Heart Problems
        - Medication Use
        - Stress Level
        - Sedentary Hours Per Day
        - BMI
        - Triglycerides
        - Physical Activity Days Per Week
        - Sleep Hours Per Day
        - Country
        - Blood pressure
    """
)

st.info(
    "All data used is anonymized and intended strictly for educational and research purposes."
)

st.header("⚙️ Data Preprocessing")

st.markdown(
    """
    - Missing values handled appropriately  
    - Categorical features encoded  
    - Numerical features scaled  
    - Handled imbalance data with SMOTE
    - Dataset split into training and testing sets
    """
)

st.header("📈 Model Performance")
st.subheader("Logistic Regression")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ROC-AUC", "~0.50")

with col2:
    st.metric("Recall", "~0.49")

with col3:
    st.metric("Accuracy", "~0.49")

st.markdown(
    """
    **Metric Interpretation:**
    - **ROC-AUC (~0.50):** Indicates no discriminative power; the model performs similarly to random guessing  
    - **Recall (~0.49):** The model fails to reliably identify high-risk patients, missing a significant portion of true cases  
    - **Accuracy (~0.49):** Overall predictions are unreliable and not better than a naive baseline  

    **Conclusion:**  
    Logistic Regression is not suitable for this dataset in its current form. This may be due to non-linear relationships, feature limitations, or class imbalance. More complex models or additional feature engineering are required to achieve meaningful performance.
    """
)

st.header("⚠️ Limitations")

st.markdown(
    """
    - The model is trained on a limited public dataset  
    - Predictions may not generalize to all populations  
    - The output should **not** be used as a medical diagnosis
    """
)
st.divider()
st.warning(
    "This application is for educational purposes only and does not replace professional medical advice."
)