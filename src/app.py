import pickle
from typing import Any, Dict

import numpy as np
import pandas as pd
import streamlit as st

from src.config import MODEL_PATH, FEATURE_COLUMNS


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model


model = load_model()

st.title("🚗 Used Car Price Prediction")
st.write("Final RandomForest pipeline'ı ile ikinci el araç liste fiyatı tahmini.")
st.subheader("Araç Bilgilerini Girin")

col1, col2 = st.columns(2)

with col1:
    brand = st.text_input("Marka (Brand)", "Toyota")
    model_name = st.text_input("Model", "Corolla")
    year = st.number_input("Yıl (Year)", min_value=1990, max_value=2025, value=2018)
    km = st.number_input("Km (kmDriven_clean)", min_value=0, max_value=500_000, value=45_000, step=1_000)

with col2:
    transmission = st.selectbox("Vites (Transmission)", ["Manual", "Automatic", "Other"])
    owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Other"])
    fuel = st.selectbox("Yakıt (FuelType)", ["Petrol", "Diesel", "CNG", "LPG", "Electric", "Other"])

CURRENT_YEAR = 2024
age = CURRENT_YEAR - int(year)
if age < 0:
    age = 0


km_per_year = km / (age + 1)
log_kmDriven = np.log1p(km)

price_per_km = 0.0

input_dict: Dict[str, Any] = {
    "Brand": brand,
    "model": model_name,
    "Year": int(year),
    "Age": float(age),
    "kmDriven_clean": float(km),
    "Transmission": transmission,
    "Owner": owner,
    "FuelType": fuel,
    "price_per_km": float(price_per_km),
    "km_per_year": float(km_per_year),
    "log_kmDriven": float(log_kmDriven),}

if st.button("Fiyat Tahmini Yap"):
    df_input = pd.DataFrame([input_dict])

    X = df_input[FEATURE_COLUMNS]

    y_pred = model.predict(X)[0]

    st.success(f"Tahmin edilen liste fiyatı: **{y_pred:,.0f} ₺**")
    st.caption("Not: Demo amaçlıdır; gerçek piyasa koşulları farklılık gösterebilir.")

