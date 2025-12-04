# 🚗 AutoML Price Prediction  
İkinci el araç pazarında, aynı marka ve modele sahip araçlar bile; yaş, kilometre, donanım, yakıt tipi, vites türü gibi özelliklere bağlı olarak çok farklı fiyatlara sahip olabilmektedir. Bu proje, araç ilanlarından elde edilen özellikleri kullanarak **piyasa değerine en yakın fiyat tahminini yapmayı** amaçlayan bir makine öğrenmesi çözümü sunar.

---

## 🔍 1. Proje Amacı

Bu projenin temel amacı; veri bilimi ve makine öğrenmesi yöntemlerini kullanarak **araç fiyat tahmini yapan uçtan uca bir model geliştirmek** ve bu süreci:

- Veri Keşfi (EDA)  
- Veri Ön İşleme  
- Feature Engineering  
- Modelleme  
- Hyperparameter Optimization  
- Final Pipeline  
- Model Kaydetme ve Yükleme  
- Deployment  

adımlarını kapsayan bir yapıya dönüştürmektir.

Bu yaklaşım, bootcamp final projesinin tüm gereksinimlerini karşılayan **tam bir ML pipeline** oluşturur.

---

## 🏭 2. Sektör Bilgisi

**Sektör:** Otomotiv / İkinci El Araç Pazarı  
**Temel Sorun:** Araç fiyatları arasındaki geniş farklılık, bilgi asimetrisi ve doğru fiyatı tahmin etme zorluğu

**Bu model ne sağlar?**

- Satıcılar için **adil ve rekabetçi fiyat önerileri**
- Alıcılar için **gerçek piyasa değerine yakın tahmin**
- Platformlar için **otomatik fiyat kontrol mekanizması**
- Sahte veya aşırı şişirilmiş ilanların tespiti

Bu sayede hem piyasa şeffaflığı artar hem de ticari süreçler daha sağlıklı yürütülür.

---

## ❓ 3. Problem Tanımı

Bir aracın teknik ve yapısal özellikleri göz önüne alındığında, gerçek piyasa değerinin belirlenmesi birçok değişkeni aynı anda dikkate almayı gerektirir.  

Bu projede amaç:

> **Araç ilanı özelliklerini (özellikle marka, model, yıl, kilometre, yakıt tipi, donanım bilgileri) kullanarak aracın satış fiyatını tahmin eden bir regresyon modeli geliştirmek.**

Hedef:

- Fiyat tahminlerindeki hata oranını (**RMSE / MAE**) düşürmek  
- Gerçekçi, genellenebilir ve esnek bir model oluşturmak  
- Tüm süreci otomasyona uygun bir pipeline’a dönüştürmek  

---

## 📂 4. Proje Yapısı (Klasörler)

project/
│
├── data/                # Ham ve işlenmiş veri setleri
├── notebooks/           # EDA, baseline, modelleme ve tuning notebookları
├── src/                 # Python scriptleri
│   ├── config.py
│   ├── pipeline.py
│   └── inference.py
│
├── models/              # Eğitilmiş modeller (.pkl / .joblib)
├── docs/                # Teorik açıklamalar, taslaklar, notlar
│
├── requirements.txt      # Projede kullanılan paketler
└── README.md             # Proje açıklama dosyası



## 📊 5. Veri Seti

**Tahmini kolonlar:**
- `brand`
- `model`
- `year`
- `mileage`
- `fuel_type`
- `transmission`
- `engine`
- `power`
- `torque`
- `owner_type`
- `price` (target)

---

## 🧠 6. Proje Akışı (Pipeline)

### **1) EDA (Exploratory Data Analysis)**
- Veri dağılımları
- Korelasyon analizi
- Eksik ve aykırı değer tespiti
- Price ilişkilerinin görsel analizi

### **2) Data Cleaning & Preprocessing**
- Eksik değer doldurma
- Outlier treatment
- Kategorik değişken encoding
- Sayısal değişken scaling

### **3) Feature Engineering**
- Araç yaşı (`car_age`)
- Yıllık km (`km_per_year`)
- Segment türetme
- One-hot veya target encoding
- Model yılı kategorileri

### **4) Baseline Model**
- Linear Regression
- Decision Tree Regressor  

### **5) Model Optimization**
- Random Forest
- XGBoost
- LightGBM  
GridSearchCV veya Optuna ile tuning

### **6) Final Pipeline**
- Preprocessing + Model tek bir Pipeline içinde
- `joblib` ile kaydedilecek

### **7) Deployment**
- Streamlit / Gradio arayüz  
- Kullanıcı girişine fiyat tahmini dönen bir model

---

## 📈 7. Beklenen Sonuçlar

- RMSE ve MAE metriklerinin iyileştirilmesi  
- Anlamlı özellikler ile açıklanabilir bir model  
- Farklı modellerin karşılaştırılması  
- Kullanıcı dostu bir demo arayüzü  

---

## 🛠 8. Kullanılan Teknolojiler

- Python  
- NumPy, Pandas  
- Scikit-learn  
- XGBoost / LightGBM  
- Matplotlib, Seaborn  
- Streamlit / Gradio  
- Git & GitHub  
- Kaggle Notebooks  

---

## 📝 9. Geliştirme Durumu 
## ✨ 10. Katkı



