import pickle
import pandas as pd
from typing import Dict, Any

from .config import MODEL_PATH, FEATURE_COLUMNS


def load_model(path: str = MODEL_PATH):
    """Eğitilmiş pipeline (preprocessor + model) dosyasını yükler."""
    with open(path, "rb") as f:
        return pickle.load(f)


def prepare_input(data: Dict[str, Any]) -> pd.DataFrame:
    """
    Tahmin için tek gözlem alır ve modelin beklediği FEATURE_COLUMNS
    sırasına göre DataFrame oluşturur.
    (Feature engineering bu fonksiyondan önce yapılmış olmalıdır.)
    """

    df = pd.DataFrame([data])

    missing = [c for c in FEATURE_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Eksik kolonlar: {missing}")

    return df[FEATURE_COLUMNS]


def predict_price(data: Dict[str, Any], model=None) -> float:
    """Tek araç için fiyat tahmini üretir."""
    if model is None:
        model = load_model()

    X = prepare_input(data)
    pred = model.predict(X)

    return float(pred[0])

