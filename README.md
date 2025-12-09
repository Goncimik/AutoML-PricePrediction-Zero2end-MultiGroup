# 🌟 Used Car Price Prediction — Zero2End AutoML Project 🚗

Bu proje, benim kapsamlı olarak ele aldığım ilk Machine Learning (ML) projesidir. 🚀

Proje, **MultiGroup Zero2End Machine Learning Bootcamp kapsamında** hazırlanmıştır.
---

---
## Proje Tanımı

Proje, otomotiv sektöründe ikinci el araçların fiyatlarını makine öğrenmesi modelleri kullanarak tahmin etmeyi amaçlayan uçtan uca (End-to-End) bir AutoML çalışmasıdır. 
Veri analizi, özellik mühendisliği, model optimizasyonu, SHAP tabanlı model yorumlama ve tam bir final pipeline yapısı içerir.

Bu projede amaç:

- Araç özelliklerinden anlamlı bilgi çıkarmak,
- Fiyatı etkileyen faktörleri ortaya koymak,
- Güvenilir bir tahmin pipeline’ı oluşturmak,
- Yorumlanabilir bir model geliştirmektir.


---

---

##  Veri Seti

**Kaggle Dataset:** Used Cars Price Prediction Dataset  
**Dosya:** `used_cars_dataset_v2.csv`  
**Kaynak:** Link: https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset

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
│   ├── 03_feature_engineering_baseline_model.ipynb
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
│   ├── 00_setup.md
│   ├── 01_data_overview.md
│   ├── 02_baseline.md
│   ├── 03_feature_engineering_baseline_model.md
│   ├── 04_model_optimization.md
│   ├── 05_model_evaluation.md
│   ├── 06_pipeline.md
│   └── final_model.md
│
├── requirements.txt
└── README.md
```

---

---

##  Proje Akışının Özeti

`notebooks/` klasöründe süreç aşağıdaki gibi ilerlemektedir:

1. **1-eda.ipynb**  
   - Veri setinin incelenmesi, eksik/aykırı değerler, dağılımlar, korelasyonlar  

2. **2-baseline.ipynb**  
   - Basit feature set ile baseline model kurulumu (Linear Regression / temel RF)  
   - İlk RMSE / MAE / R² sonuçları  

3. **3-feature-engineering-baseline-model.ipynb**  
   - price_per_km, log_kmDriven, km_per_year gibi yeni feature’ların türetilmesi  
   - FE sonrası performansın baseline ile karşılaştırılması  

4. **4-model-optimization.ipynb**  
   - RandomForest, XGBoost ve LightGBM modellerinin denenmesi  
   - Validation set üzerinde model karşılaştırması  
   - En iyi modelin seçilmesi (RandomForest)  

5. **5-model-evaluation.ipynb**  
   - Final modelin performans metrikleri  
   - Feature importance  
   - SHAP ile model açıklanabilirliği  

6. **6-pipeline.ipynb**  
   - Preprocess + model → tek pipeline  
   - Train / Validation / Test ayrımı  
   - Test performansı  

7. **final-model.ipynb**  
   - Data leakage tespiti (log_price) ve düzeltilmesi  
   - Düzeltilmiş feature set ile modellerin yeniden eğitilmesi  
   - Final RandomForest modelinin seçimi  
   - Test sonuçları  
   - Model kaydetme (pickle)  
   - Tahmin fonksiyonu (`predict_car_price`)

---

---

##  Final Model Performansı

RandomForest modeli; performans, açıklanabilirlik ve stabilite açısından final model olarak seçilmiştir.

Final model: **RandomForest Regressor**

**Test Set Sonuçları:**  
- **MAE:** ~34,000  
- **RMSE:** ~345,000  
- **R²:** ~0.94  

Model fiyat varyansının büyük kısmını açıklamakta ve pratik anlamda yüksek doğruluk sağlamaktadır.

---

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

---
## Deployment 

- Streamlit
  
- **Deployment Notu**

-  PKL dosyası boyut limiti yüzünden repoya eklenemedi ve model Streamlit üzerinde yeniden eğitilmeye çalışıldı. Ama bu Streamlit deployment denemesinde de veri uyumsuzlukları, CSV dosyasının cloud ortamında bulunamaması ve model-pipeline ilişkisi gibi hatalar nedeniyle uygulama çevrimiçi olarak çalıştırılamadı. Uygulama bu nedenle yalnızca lokal ortamda stabil şekilde çalışacak biçimde bırakıldı. Bu projenin bir kısıtıdır ve bu kısıt ilerleyen süreçlerde yeniden ele alınacaktır.
---

---

## Teknolojiler

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- LightGBM
- SHAP
- Matplotlib 
- Seaborn
- Pickle
- Streamlit 

---

---

##  Kurulum

```bash
git clone https://github.com/Goncimik/AutoML-PricePrediction-Zero2end-MultiGroup.git
cd AutoML-PricePrediction-Zero2end-MultiGroup
pip install -r requirements.txt
```

---

---
## Inference 

```python
from src.inference import predict_price

sample = {
    "brand": "BMW",
    "year": 2018,
    "kmDriven": 85000,
    "fuel": "Diesel",
    "transmission": "Automatic"}

print(predict_price(sample))
```

---

---

##  Notlar

- Proje uçtan uca AutoML sürecini kapsar.  
- Notebook’lar adım adım geliştirmenin izlenebilmesi için bölümlendirilmiştir.  
- Final model pipeline yapısı script olarak (`src/pipeline.py`) kodlanmıştır.  

---

---

##  İletişim

Geliştirmeler, katkılar veya öneriler için issue/pull request açabilirsiniz.

## Son
-  **Mutlu Kodlamalar** 💫
- 🌟 🚗 🤖  



