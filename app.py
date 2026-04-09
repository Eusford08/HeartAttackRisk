import streamlit as st


# Page config
st.set_page_config(
    page_title="Heart Attack Prediction",
    page_icon="❤️"
)

# Navigation
pg = st.navigation({
    "Main": [
        st.Page(
            "pages/index.py",
            title="Home",
            icon=":material/home:"
        ),
        st.Page(
            "pages/predict_new_model.py",
            title="Predict (New Model)",
            icon=":material/edit:"
        ),
        st.Page(
            "pages/predict_old_model.py",
            title="Predict (Old Model)",
            icon=":material/edit:"
        ),
    ],
    "About": [
        st.Page(
            "pages/about_new_model.py",
            title="New Model Info",
            icon=":material/smart_toy:"
        ),
        st.Page(
            "pages/about_old_model.py",
            title="Old Model Info",
            icon=":material/smart_toy:"
        ),
    ],
})

pg.run()