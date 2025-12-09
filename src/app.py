import numpy as np
import pandas as pd
import streamlit as st

from src.config import FEATURE_COLUMNS
from src.pipeline import load_and_fe, split_data, train_pipeline




@st.cache_resource
def load_model():
    """Veriyi yükler, FE uygular, modeli eğitir ve cache'ler."""
    df = load_and_fe()
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)
    model = train_pipeline(X_train, y_train)
    return model


model = load_model()

st.title("🚗 Kullanılmış Araç Fiyat Tahmini")
st.write("Bu uygulama, eğitilmiş RandomForest modelini kullanarak ikinci el araç fiyatı tahmini yapar.")

st.subheader("Araç Bilgilerini Girin")

col1, col2 = st.columns(2)

with col1:
    brand = st.text_input("Marka (Brand)", "Toyota")
    model_name = st.text_input("Model", "Corolla")
    year = st.number_input("Model Yılı (Year)", 1990, 2025, 2018)
    km = st.number_input("Kilometre (kmDriven_clean)", 0, 500_000, 45_000, step=1_000)

with col2:
    transmission = st.selectbox("Vites (Transmission)", ["Manual", "Automatic"])
    owner = st.selectbox("Sahiplik (Owner)", ["First Owner", "Second Owner", "Other"])
    fuel = st.selectbox("Yakıt Tipi (FuelType)", ["Petrol", "Diesel", "LPG", "CNG", "Hybrid"])


CURRENT_YEAR = 2024
age = max(0, CURRENT_YEAR - int(year))


km_per_year = km / (age + 1)
log_km = np.log1p(km)
price_per_km = 0.0  


if st.button("Fiyat Tahmini Yap"):
    sample = {
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
        "log_kmDriven": float(log_km),}

    df_input = pd.DataFrame([sample])[FEATURE_COLUMNS]
    y_pred = model.predict(df_input)[0]

    st.success(f"💰 Tahmini Araç Fiyatı: **{y_pred:,.0f} ₺**")
    st.caption("Not: Demo amaçlıdır; gerçek piyasa koşulları ve ilan fiyatları farklılık gösterebilir.")
