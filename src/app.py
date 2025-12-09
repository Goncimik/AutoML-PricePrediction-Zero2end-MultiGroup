import pickle
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

def preprocess_input(user_input: dict) -> pd.DataFrame:
    """
    Kullanıcıdan alınan input'u DataFrame’e çevirir.
    Pipeline içindeki preprocessing adımları zaten modelin içinde.
    """
    df = pd.DataFrame([user_input])
    return df

st.title("🚗 Kullanılmış Araç Fiyat Tahmini")
st.write("Bu uygulama, eğitilmiş RandomForest modelinizi kullanarak araç fiyatı tahmini yapar.")

brand = st.selectbox("Marka", ["BMW", "Mercedes", "Audi", "Volkswagen", "Renault", "Toyota", "Hyundai"])
model_name = st.text_input("Model Adı")
year = st.number_input("Model Yılı", 1990, 2025, 2015)
age = 2025 - year
km = st.number_input("Kilometre (km)", 0, 500000, 120000)
fuel = st.selectbox("Yakıt Tipi", ["Petrol", "Diesel", "LPG", "Hybrid"])
trans = st.selectbox("Vites", ["Manual", "Automatic"])
owner = st.selectbox("Sahiplik Sayısı", ["First Owner", "Second Owner", "Third Owner"])


price_per_km = 0  
km_per_year = km / (age + 1)
log_km = np.log1p(km)


if st.button("Fiyat Tahmini Yap"):
    sample = {
        "Brand": brand,
        "model": model_name,
        "Year": year,
        "Age": age,
        "kmDriven_clean": km,
        "Transmission": trans,
        "Owner": owner,
        "FuelType": fuel,
        "price_per_km": price_per_km,
        "km_per_year": km_per_year,
        "log_kmDriven": log_km }

    df_input = preprocess_input(sample)
    prediction = model.predict(df_input)[0]

    st.success(f"💰 Tahmini Araç Fiyatı: **{prediction:,.0f} ₺**")
