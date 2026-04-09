import streamlit as st
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
MODEL_DIR = BASE_DIR / "model"

@st.cache_resource
def load_old_model():
    print("🔥 Loading Old model")
    return joblib.load(MODEL_DIR / "oldHeartAttackRisk_model.pkl")

@st.cache_resource
def load_new_model():
    print("🔥 Loading New model")
    return joblib.load(MODEL_DIR / "newHeartAttackRisk_model.pkl")

