
DATA_PATH = "data/used_cars_dataset_v2.csv"
MODEL_PATH = "models/final_car_price_model.pkl"


TARGET = "AskPrice_clean"

BASE_FEATURES = [
    "Brand",
    "model",
    "Year",
    "Age",
    "kmDriven_clean",
    "Transmission",
    "Owner",
    "FuelType",]


ENGINEERED_FEATURES = [
    "price_per_km",
    "km_per_year",
    "log_kmDriven",]


FEATURE_COLUMNS = BASE_FEATURES + ENGINEERED_FEATURES

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


FIRST_SPLIT_TEST_SIZE = 0.30 
SECOND_SPLIT_TEST_SIZE = 0.50  

RANDOM_STATE = 42


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

BEST_MODEL_NAME = "RandomForest"

