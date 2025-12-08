# 00 | Setup

Bu doküman, AutoML Price Prediction projesini yerel ortamında çalıştırmak için gerekli kurulum adımlarını ve proje yapısını özetler.

---

## 1. Önkoşullar (Prerequisites)

Projeyi çalıştırmak için aşağıdaki bileşenlere ihtiyacın vardır:

- **Python 3.10+**
- **Git**
- İnternet bağlantısı (gerekli paketleri indirmek için)
- (Opsiyonel) IDE / Notebook ortamı:
  - VS Code, PyCharm veya JupyterLab / Jupyter Notebook

---

## 2. Depoyu Klonlama

Önce projeyi GitHub’dan yerel makineye indir:

```bash
git clone https://github.com/Goncimik/AutoML-PricePrediction-Zero2end-MultiGroup.git
cd AutoML-PricePrediction-Zero2end-MultiGroup
```

---

## 3. Sanal Ortam (Virtual Environment) Oluşturma

Proje bağımlılıklarını izole bir ortamda tutmak için sanal ortam kullanılması tavsiye edilir.

### 3.1. Windows (PowerShell / CMD)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3.2. macOS / Linux (bash / zsh)

```bash
python -m venv .venv
source .venv/bin/activate
```

Aktif ettikten sonra komut satırında başta `(venv)` veya `(.venv)` görmelisin.

---

## 4. Bağımlılıkların Kurulumu

Projede kullanılan Python paketlerini kurmak için:

```bash
pip install -r requirements.txt
```

> Not: `requirements.txt` dosyası, EDA, modelleme, optimizasyon ve değerlendirme aşamalarında kullanılan temel kütüphaneleri içerecek şekilde güncellenmelidir:
> - pandas, numpy  
> - scikit-learn  
> - xgboost, lightgbm  
> - matplotlib, seaborn  
> - shap  
> - jupyter / notebook

---

## 5. Notebook’ları Çalıştırma

Uçtan uca süreci adım adım izlemek için `notebooks/` klasöründeki dosyaları kullanabilirsin.

```bash
jupyter notebook
```

veya

```bash
jupyter lab
```

Ardından sırasıyla aşağıdaki notebook’ları aç:

1. `1-eda.ipynb`  
2. `2-baseline.ipynb`  
3. `3-feature-engineering-baseline-model.ipynb`  
4. `4-model-optimization.ipynb`  
5. `5-model-evaluation.ipynb`  
6. `6-pipeline.ipynb`  
7. `final-model.ipynb`

Bu sıralama, bootcamp final projesinin beklediği EDA → Baseline → Feature Engineering → Model Optimization → Evaluation → Pipeline → Final Model akışıyla uyumludur.

---

## 6. Kaydedilmiş Modeller ve Tahmin

Eğitim sonrası oluşan modeller:

- **Klasör:** `models/`  
  - Örnek: `final_car_price_model.pkl`

Bu model, `src/` içindeki yardımcı script’ler veya notebook’lar üzerinden yüklenerek tahmin amaçlı kullanılabilir.

---

## 7. Kaynak Kod (src/)

`src/` klasörü, proje kodlarının modüler hâlini içerir:

- `src/config.py`  
  - Proje boyunca kullanılan sabitler, yol tanımları ve genel ayarlar

- `src/pipeline.py`  
  - Veri ön işleme (preprocessing) ve model eğitim pipeline’ı
  - Train / validation / test akışının fonksiyonel hâli

- `src/inference.py`  
  - Kaydedilmiş modeli yükleyip yeni bir araç için fiyat tahmini yapan fonksiyonlar
  - Örnek: API, CLI veya Streamlit arayüzü için kullanılabilir

Bu dosyalar, notebook’ta yaptığın işlemlerin daha üretim odaklı, tekrar kullanılabilir hâle getirilmiş versiyonlarıdır.

---

## 8. Proje Klasör Yapısı (Özet)

```text
AutoML-PricePrediction-Zero2end-MultiGroup/
├── data/           # Ham ve işlenmiş veri setleri
├── notebooks/      # 1-EDA, 2-Baseline, 3-FE, 4-Model Opt, 5-Eval, 6-Pipeline, final-model
├── src/            # config, pipeline, inference vb. Python scriptleri
├── models/         # Eğitilmiş modeller (.pkl / .joblib)
├── docs/           # Proje dokümantasyonu (00_setup + 01-07 teknik açıklamalar)
├── requirements.txt
└── README.md
```

---

## 9. Çalıştırma Özet Adımları

Kısaca:

1. Depoyu klonla  
2. Sanal ortam oluştur ve aktive et  
3. `pip install -r requirements.txt`  
4. `jupyter lab` veya `jupyter notebook` ile `notebooks/` içindeki dosyaları sırayla çalıştır  
5. Eğitilen modeli `models/` klasöründen yükleyerek `src/inference.py` içinde tahmin fonksiyonlarıyla kullan

Bu adımlar tamamlandığında, proje uçtan uca (EDA → Model → Pipeline → Final Model) çalışır hâle gelecektir.

