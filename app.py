import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------- DARK THEME CSS ----------------
st.markdown("""
    <style>

    /* App Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0E1117 0%, #111827 100%);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Title */
    .title {
        font-size: 4vw !important;
        font-weight: 800 !important;
        color: #00E0FF !important;
        line-height: 1.2 !important;
    }

    .subtext {
        font-size:18px;
        color:#9CA3AF;
    }

    /* Section Headers */
    h3 {
        color: #E5E7EB;
    }

    /* Inputs */
    .stNumberInput input, 
    .stSelectbox div[data-baseweb="select"], 
    .stSlider {
        background-color: #161B22 !important;
        color: white !important;
    }

    /* Button */
    .stButton>button {
        background: linear-gradient(90deg, #00E0FF, #007CF0);
        color: white;
        font-size:18px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        border: none;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        transition: 0.2s ease;
    }

    /* Divider */
    hr {
        border: 1px solid rgba(255,255,255,0.1);
    }

    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="title">🏠 Smart House Price Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Enter house details and get instant AI-based prediction</p>', unsafe_allow_html=True)

st.write("")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model/model.pkl", "rb"))

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Enter Property Details")

    area = st.number_input("Area (sqft)", 500, 10000, 1500)
    bedrooms = st.number_input("Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("Bathrooms", 1, 10, 2)
    floors = st.number_input("Floors", 1, 5, 1)

with col2:
    st.subheader("🏘 Additional Features")

    age = st.number_input("Age of House (Years)", 0, 100, 5)
    garage = st.selectbox("Garage Available?", ["No", "Yes"])
    location_score = st.slider("Location Score (1-10)", 1, 10, 5)

# Convert Garage to numeric
garage_value = 1 if garage == "Yes" else 0

st.write("")
st.write("")

# ---------------- PREDICTION BUTTON ----------------
if st.button("🚀 Predict House Price"):

    input_data = np.array([[area, bedrooms, bathrooms, floors, age, garage_value, location_score]])
    prediction = model.predict(input_data)

    st.markdown("---")
    st.success(f"💰 Estimated House Price: ₹ {prediction[0]:,.2f}")
    st.balloons()