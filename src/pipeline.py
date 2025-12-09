import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

from .config import (
    DATA_PATH,
    MODEL_PATH,
    FEATURE_COLUMNS,
    CATEGORICAL_COLS,
    NUMERICAL_COLS,
    TARGET,
    FIRST_SPLIT_TEST_SIZE,
    SECOND_SPLIT_TEST_SIZE,
    RANDOM_STATE,
    RF_PARAMS)


def load_and_fe():
    df = pd.read_csv(DATA_PATH).copy()


    df["price_per_km"] = df[TARGET] / (df["kmDriven_clean"] + 1)
    df["km_per_year"] = df["kmDriven_clean"] / (df["Age"] + 1)
    df["log_kmDriven"] = np.log1p(df["kmDriven_clean"])

  
    if "log_price" in df:
        df = df.drop(columns=["log_price"])

    return df

def split_data(df):
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y,
        test_size=FIRST_SPLIT_TEST_SIZE,
        random_state=RANDOM_STATE)

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp,
        test_size=SECOND_SPLIT_TEST_SIZE,
        random_state=RANDOM_STATE)

    return X_train, X_val, X_test, y_train, y_val, y_test

def build_preprocessor():
    return ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_COLS),
            ("num", "passthrough", NUMERICAL_COLS),])
 
def train_pipeline(X_train, y_train):
    preprocessor = build_preprocessor()

    model = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", RandomForestRegressor(**RF_PARAMS))])

    model.fit(X_train, y_train)
    return model

def save_model(model, path=MODEL_PATH):
    with open(path, "wb") as f:
        pickle.dump(model, f)

def run():
    print("📌 Veri yükleniyor ve FE uygulanıyor...")
    df = load_and_fe()

    print("📌 Train/Val/Test split yapılıyor...")
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)

    print("📌 Model pipeline eğitiliyor...")
    model = train_pipeline(X_train, y_train)

    print("📌 Model kaydediliyor...")
    save_model(model)

    print("🎉 Pipeline tamamlandı! Model kaydedildi →", MODEL_PATH)


if __name__ == "__main__":
    run()
