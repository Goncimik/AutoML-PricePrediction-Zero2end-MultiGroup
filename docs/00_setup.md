# 00 | Setup

Bu doküman, AutoML Price Prediction projesini yerel ortamda çalıştırmak için gerekli kurulum adımlarını ve proje yapısını özetler.

---

## 1. Önkoşullar (Prerequisites)

Projeyi çalıştırmak için:

- Python 3.10+
- Git
- İnternet bağlantısı
- (Tercihen) VS Code, PyCharm veya JupyterLab / Jupyter Notebook

---

## 2. Depoyu Klonlama

Projeyi GitHub’dan bilgisayarına çek:

```bash
git clone https://github.com/Goncimik/AutoML-PricePrediction-Zero2end-MultiGroup.git
cd AutoML-PricePrediction-Zero2end-MultiGroup
```

---

## 3. Sanal Ortam (Virtual Environment)

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 4. Gerekli Paketlerin Kurulumu

Projede kullanılan Python paketlerini kur:

```bash
pip install -r requirements.txt
```

`requirements.txt` içinde temel olarak şunlar yer almalıdır:

- pandas  
- numpy  
- scikit-learn  
- xgboost  
- lightgbm  
- matplotlib, seaborn  
- shap  
- joblib  
- jupyter, notebook  

---

## 5. Veri Seti

Proje, ikinci el araç fiyat tahmini için Kaggle’daki **Used Car Price Dataset** verisini kullanır:

- Kaggle veri seti:  
  `https://www.kaggle.com/datasets/ananthr1/used-car-price-dataset`

Veri dosyaları yerel ortamda:

- `data/` klasörü altında tutulur.

---

## 6. Notebook’ların Çalıştırılması

Tüm deneysel çalışma ve adım adım süreç `notebooks/` klasöründedir.

Jupyter’i başlat:

```bash
jupyter notebook
```

veya

```bash
jupyter lab
```

Ardından aşağıdaki sıralamayla notebook’ları çalıştır:

1. `1-eda.ipynb`  
2. `2-baseline.ipynb`  
3. `3-feature-engineering-baseline-model.ipynb`  
4. `4-model-optimization.ipynb`  
5. `5-model-evaluation.ipynb`  
6. `6-pipeline.ipynb`  
7. `final-model.ipynb`

Bu akış, EDA → Baseline → Feature Engineering → Model Optimization → Evaluation → Pipeline → Final Model şeklindeki uçtan uca süreci temsil eder.

---

## 7. Modeller (models/ klasörü)

Eğitilmiş modeller:

- `models/` klasörü altında saklanır.
- Örnek:  
  - `final_car_price_model.pkl` → leakage düzeltilmiş feature set ile eğitilmiş **final RandomForest modeli**.

Bu dosya, `src/inference.py` veya notebook’lar içinde yüklenerek tahmin amaçlı kullanılır.

---

## 8. Kaynak Kodlar (src/ klasörü)

`src/` klasörü, notebook’larda yaptığın işlemlerin modüler Python versiyonlarını içerir:

- `src/config.py` → yol tanımları, genel ayarlar, random_state vb.
- `src/pipeline.py` → veri ön işleme ve model pipeline fonksiyonları
- `src/inference.py` → `models/final_car_price_model.pkl` dosyasını yükleyip yeni bir araç için fiyat tahmini yapan fonksiyon(lar)

---

## 9. Klasör Yapısı Özeti

```text
AutoML-PricePrediction-Zero2end-MultiGroup/
├── data/           # Ham ve işlenmiş veri setleri
├── notebooks/      # 1–7 arası tüm ML süreci
├── src/            # config, pipeline, inference
├── models/         # Eğitilmiş modeller (.pkl)
├── docs/           # 00_setup + 01–07 teknik dokümanlar
├── requirements.txt
└── README.md
```

---

## 10. Hızlı Çalıştırma Özeti

Kısaca tüm adımlar:

```bash
git clone https://github.com/Goncimik/AutoML-PricePrediction-Zero2end-MultiGroup.git
cd AutoML-PricePrediction-Zero2end-MultiGroup
python -m venv .venv
# ortamı aktif et
pip install -r requirements.txt
jupyter notebook
```

Bu adımlardan sonra, notebook’ları sırayla çalıştırarak projeyi uçtan uca yeniden üretebilirsin.

