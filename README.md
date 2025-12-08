# 🚗 Used Car Price Prediction — Zero2End AutoML Project

Bu proje, ikinci el araçların fiyatlarını makine öğrenmesi modelleri kullanarak tahmin etmeyi amaçlayan uçtan uca (End-to-End) bir AutoML çalışmasıdır. Veri analizi, özellik mühendisliği, model optimizasyonu, SHAP tabanlı model yorumlama ve tam bir final pipeline yapısı içerir.

---

##  Veri Seti

**Kaggle Dataset:** Used Cars Price Prediction Dataset  
**Dosya:** `used_cars_dataset_v2.csv`  
**Kaynak:** https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset  

Temel değişkenler:  
- **Make/Model**  
- **Year**  
- **kmDriven**  
- **Fuel Type**  
- **Transmission**  
- **Owner Type**  
- **AskPrice** (hedef değişken)  

Veri seti yaklaşık **15.000 gözlem** içermektedir ve hem kategorik hem sayısal değişkenlerden oluşmaktadır.

---

##  Proje Yapısı

```
AutoML-PricePrediction-Zero2end-MultiGroup/
│
├── data/
│   └── used_cars_dataset_v2.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_optimization.ipynb
│   ├── 05_model_evaluation.ipynb
│   ├── 06_pipeline.ipynb
│   └── 07_final_model.ipynb
│
├── src/
│   ├── config.py
│   ├── pipeline.py
│   └── inference.py
│
├── models/
│   └── final_model.pkl
│
├── docs/
│   ├── eda.md
│   ├── baseline.md
│   ├── feature_engineering.md
│   ├── model_optimization.md
│   ├── model_evaluation.md
│   ├── pipeline.md
│   └── final_model.md
│
├── requirements.txt
└── README.md
```

---

##  Proje Akışının Özeti

1. **EDA (01_eda.ipynb)**  
   - Veri analizi  
   - Eksik/aykırı değerler  
   - Dağılımlar & korelasyon  

2. **Baseline (02_baseline.ipynb)**  
   - İlk model ve ilk skorlar  
   - Baseline değerlendirmesi  

3. **Feature Engineering (03_feature_engineering.ipynb)**  
   - age, km_per_year, price_per_km, log dönüşümleri  
   - Feature etkilerinin analizi  

4. **Model Optimization (04_model_optimization.ipynb)**  
   - RandomForest, XGBoost, LightGBM  
   - Hiperparametre araması  

5. **Model Evaluation  (05_model_evaluation.ipynb)**  
   - Feature importance  
   - SHAP summary & dependence  

6. ** Pipeline (06_pipeline.ipynb)**  
   - Final feature set  
   - Final model eğitimi  
   - Test set performansı  
   - Model kaydetme & inference örnekleri  

---

##  Final Model Performansı

Final model: **RandomForest Regressor**

**Test Set Sonuçları:**  
- **MAE:** ~34,000  
- **RMSE:** ~345,000  
- **R²:** ~0.94  

Model fiyat varyansının büyük kısmını açıklamakta ve pratik anlamda yüksek doğruluk sağlamaktadır.

---

##  Açıklanabilirlik (Explainability)

SHAP analizleri ile:

- price_per_km  
- kmDriven  
- age  
- year  
- premium marka etkileri  

gibi değişkenlerin fiyat tahminine yön veren ana faktörler olduğu doğrulanmıştır. 

---

##  Kurulum

```bash
git clone https://github.com/Goncimik/AutoML-PricePrediction-Zero2end-MultiGroup.git
cd AutoML-PricePrediction-Zero2end-MultiGroup
pip install -r requirements.txt
```

---

##  Tahmin Alma (Inference)

```python
from src.inference import predict_price

sample = {
    "brand": "BMW",
    "year": 2018,
    "kmDriven": 85000,
    "fuel": "Diesel",
    "transmission": "Automatic"
}

print(predict_price(sample))
```

---

##  Notlar

- Proje uçtan uca AutoML sürecini kapsar.  
- Notebook’lar adım adım geliştirmenin izlenebilmesi için bölümlendirilmiştir.  
- Final model pipeline yapısı script olarak (`src/pipeline.py`) kodlanmıştır.  

---

##  İletişim

Geliştirmeler, katkılar veya öneriler için issue/pull request açabilirsiniz.




