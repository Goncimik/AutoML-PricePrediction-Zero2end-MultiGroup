# Proje ayarları

DATA_PATH = "data/used_car_dataset_v2.csv"
MODEL_PATH = "models/final_car_price_model.pkl"

TARGET = "Price"

FEATURE_COLUMNS = [
    "Brand", "Model", "Year", "Age", "KmDriven",
    "FuelType", "Transmission", "Owner", "Mileage",
    "Engine", "MaxPower", "Seats"]

CATEGORICAL_COLS = ["Brand", "Model", "FuelType", "Transmission", "Owner"]
NUMERICAL_COLS = ["Year", "Age", "KmDriven", "Mileage", "Engine", "MaxPower", "Seats"]

TEST_SIZE = 0.2
RANDOM_STATE = 42
