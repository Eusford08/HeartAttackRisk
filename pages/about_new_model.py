import streamlit as st

st.set_page_config(page_title="Model Information", layout="centered", page_icon="🧠")

st.title("📊 Main Model & Dataset Information", anchor=False)

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
    - **Model Type:** Random Forest  
    - **Task:** Binary Classification (Heart Attack Risk: Yes / No)  

    - **Rationale for Selection:**  
      - **Captures Non-Linear Relationships:** Effectively models complex interactions between clinical features  
      - **Robust to Noise & Outliers:** Ensemble averaging reduces variance and improves stability  
      - **Strong Predictive Performance:** Often outperforms single models on tabular medical datasets  
      - **Reduced Overfitting Risk:** Combines multiple decision trees to generalize better than individual trees  
      - **Feature Importance Insight:** Provides relative importance of features, supporting interpretability at a global level  
    """
)

st.header("📁 Dataset Information")

st.markdown(
    """
    - **Source:** https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset  
    - **Number of Samples:** ~8763 records  
    - **Target Variable:** Heart attack Risk  
    - **Target Variable Derivation:** Created using unsupervised learning with K-means clustering, separating the data into 2 clusters.  
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
st.subheader("Random Forest")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ROC-AUC", "1.00")

with col2:
    st.metric("Recall", "1.00")

with col3:
    st.metric("Accuracy", "1.00")

st.markdown(
    """
    **Metric Interpretation:**
    - **ROC-AUC (1.00):** Perfect class separability  
    - **Recall (1.00):** All high-risk cases are correctly identified  
    - **Accuracy (1.00):** All predictions are correct  

    **Important Note:**  
    These perfect scores are expected because the target variable was derived from clustering results (unsupervised learning).  
    The model is effectively learning to reproduce patterns that were already defined by the clustering algorithm, leading to near-perfect performance.

    **Implication:**  
    This does not reflect real-world predictive capability. The results demonstrate consistency with the clustering structure rather than true generalization to unseen data.

    **Conclusion:**  
    This model should be interpreted as a validation of clustering separability, not as a production-ready predictive model. A proper supervised target (e.g., actual heart attack outcomes) is required for meaningful evaluation.
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