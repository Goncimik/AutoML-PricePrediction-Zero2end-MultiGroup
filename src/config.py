# =========================
# 1) Dosya yolları
# =========================

# Veri seti CSV yolu (lokal repo içi)
DATA_PATH = "data/used_cars_dataset_v2.csv"

# Eğitilmiş final model dosyasının yolu (repo içi)
MODEL_PATH = "models/final_car_price_model.pkl"


# =========================
# 2) Hedef değişken
# =========================
TARGET = "AskPrice_clean"


# =========================
# 3) Feature listeleri
# =========================
BASE_FEATURES = [
    "Brand",
    "model",
    "Year",
    "Age",
    "kmDriven_clean",
    "Transmission",
    "Owner",
    "FuelType",]

# df_fe’de türetilen ek değişkenler
ENGINEERED_FEATURES = [
    "price_per_km",
    "km_per_year",
    "log_kmDriven",]

# Final modelde kullanılan tüm feature’lar
FEATURE_COLUMNS = BASE_FEATURES + ENGINEERED_FEATURES

# Kategorik / sayısal kolon ayrımı 
CATEGORICAL_COLS = [
    "Brand",
    "model",
    "Transmission",
    "Owner",
    "FuelType",]

NUMERICAL_COLS = [
    "Year",
    "Age",
    "kmDriven_clean",
    "price_per_km",
    "km_per_year",
    "log_kmDriven",]


# =========================
# 4) Veri bölme (train / val / test)
# =========================
FIRST_SPLIT_TEST_SIZE = 0.30   # train %70, temp %30
SECOND_SPLIT_TEST_SIZE = 0.50  # temp’in yarısı val, yarısı test  (~%15 / %15)

RANDOM_STATE = 42


# =========================
# 5) Model hiperparametreleri
# =========================
RF_PARAMS = {
    "n_estimators": 300,
    "random_state": RANDOM_STATE,
    "n_jobs": -1,}

XGB_PARAMS = {
    "n_estimators": 300,
    "learning_rate": 0.1,
    "max_depth": 6,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "random_state": RANDOM_STATE,
    "n_jobs": -1,
    "tree_method": "hist",}

LGBM_PARAMS = {
    "n_estimators": 300,
    "learning_rate": 0.1,
    "random_state": RANDOM_STATE,
    "n_jobs": -1,}

# Validation’da en iyi performans veren model
BEST_MODEL_NAME = "RandomForest"

