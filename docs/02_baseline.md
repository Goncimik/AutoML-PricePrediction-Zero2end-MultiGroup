# 02 | Baseline Model

Bu bölümde, ikinci el araç fiyat tahmini problemi için oluşturulan baseline modelinin tüm adımları özetlenmektedir. Baseline modeli, minimum feature engineering ile hızlı bir başlangıç performansı elde etmek ve sonraki gelişmiş modeller için karşılaştırma zemini oluşturmak amacıyla kullanılmıştır.

---

## 2.1 Baseline Feature Set ve Hedef Değişken

Baseline aşamasında yalnızca temel dönüşümü yapılmış, doğrudan kullanılabilir değişkenler kullanılmıştır. Notebook içeriğine göre baseline’da kullanılan değişkenler:

- Year — aracın üretim yılı
- Age — aracın yaşı (türetilmiş temel değişken)
- kmDriven_clean — temizlenmiş kilometre bilgisi
- AskPrice_clean — hedef değişken (temizlenmiş fiyat)

Bu aşamada gelişmiş feature engineering uygulanmamıştır. Hedef: Maksimum basitlik + hızlı benchmark.

---

## 2.2 Baseline Modelin Eğitimi

### Train–Test Ayrımı
Notebook’ta veri şu şekilde %80 eğitim ve %20 test olarak ayrılmıştır:

- test_size = 0.20  
- random_state = 42  
- shuffle = True  

### Kullanılan Model

Baseline model bir scikit-learn Pipeline kullanılarak kurulmuştur:

- Kategorik değişkenler → OneHotEncoder  
- Sayısal değişkenler → StandardScaler  
- Tahminleyici → LinearRegression  

Pipeline yapısı daha sonra üretim ortamında kullanılabilirliği kolaylaştırmaktadır.

---

## 2.3 Baseline Model Performansı

Notebook'ta aşağıdaki performans metrikleri hesaplanmıştır:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Skoru

Elde edilen sonuçlar baseline model için beklenen seviyededir:

- RMSE’nin yüksek olması fiyatlarda geniş bir varyans bulunduğunu gösterir.  
- MAE orta düzeyde olup temel hatayı doğru yansıtır.  
- R² skorunun düşük/orta seviyede olması, gelişmiş modellere ihtiyaç olduğunu doğrulamaktadır.

---

## 2.4 Cross-Validation Sonuçları

Baseline modeli 5 katlı KFold cross-validation ile değerlendirilmiştir:

- n_splits = 5  
- shuffle = True  
- random_state = 42  

Sonuçlar:

- Her fold için R² skorları
- Ortalama R² skoru

Bu skorlar baseline performansının stabil olduğunu göstermektedir.

---

## 2.5 Baseline Özet Bulgular

- Baseline model hızlı, basit ve referans niteliğinde bir başlangıç noktası sağlamaktadır.  
- Age, Year ve kmDriven değişkenleri fiyat tahmininde önemli rol oynamaktadır.  
- Lineer model, ilişkileri sınırlı düzeyde yakalayabildiği için performans kısıtlı kalmıştır.  
- Sonuçlar, feature engineering ve model optimizasyonu ile dikkate değer bir iyileşme potansiyeli olduğunu göstermektedir.

Baseline aşaması başarıyla tamamlanmış olup sonraki gelişmiş modelleme adımlarına sağlam bir temel oluşturmuştur.

