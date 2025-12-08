# 03 | Feature Engineering

Bu bölümde, ikinci el araç fiyat tahmini için kullanılan veri seti üzerinde uygulanan feature engineering işlemleri açıklanmaktadır.
---

## 3.1 Modelleme İçin Veri Hazırlığı

Notebook’ta modelleme için seçilen temel değişkenler:

- **Brand**
- **model**
- **Year**
- **Age**
- **kmDriven_clean**
- **AskPrice_clean** (hedef)

Bu kolonlar kullanılarak şu şekilde bir modelleme veri seti oluşturulmuştur:

- `df_model = df[["Brand", "model", "Year", "Age", "kmDriven_clean", "AskPrice_clean"]].copy()`

Bu aşamada henüz yeni türetilmiş feature yoktur; amaç temiz ve temel bir veri yapısı hazırlamaktır.

---

## 3.2 Başlangıç Train–Test Ayrımı

İlk aşamada veri **train** ve **test** olarak ikiye ayrılmıştır. Notebook çıktısına göre:

- Train set: **11.924 satır**, **8 feature**
- Test set: **2.981 satır**, **8 feature**

Notebook çıktısı:

```text
((11924, 8), (2981, 8))
```

Bu ayrım baseline değerlendirmesi için kullanılmış, daha sonra feature engineering sonrası 3’lü (train/val/test) yapıya geçilmiştir.

---

## 3.3 Kategorik Encoding ve Baseline Pipeline

Kategorik ve sayısal kolonlar ayrılmıştır:

- Kategorik kolonlar:
  - `Brand`
  - `model`
  - `Transmission`
  - `Fuel`

- Sayısal kolonlar:
  - `Year`
  - `Age`
  - `kmDriven_clean`

Bu kolonlar için **OneHotEncoder** ve **StandardScaler** içeren bir **scikit-learn `Pipeline`** tanımlanmıştır. Model olarak **LinearRegression** kullanılmıştır. Pipeline yapısı, ön işleme ve model eğitimini tek akışta birleştirecek şekilde tasarlanmıştır.

---

## 3.4 Baseline Model Test Performansı

İlk baseline model, temel feature set ile eğitilmiş ve test seti üzerinde değerlendirilmiştir. Notebook çıktısına göre:

```text
(1639474415726.2817,
 1280419.6248598667,
 538396.9695133752,
 0.36600805642698875)
```

Bu değerler sırasıyla:

- **MSE:** 1,639,474,415,726.28  
- **RMSE:** 1,280,419.62  
- **MAE:** 538,396.97  
- **R²:** 0.3660  

Bu sonuçlar, baseline modelin fiyat varyansını tam olarak açıklayamadığını ve hem feature engineering hem de optimizasyona ihtiyaç olduğunu göstermektedir.

---

## 3.5 Baseline Model Cross-Validation Sonuçları

Baseline model, 5 katlı K-Fold cross-validation ile değerlendirilmiştir. Notebook çıktısı:

```text
(array([0.36600805, 0.40504958, 0.27251369, 0.40337956, 0.36061624]),
 0.3615134245242876)
```

Buna göre:

- Katman bazlı R² skorları:
  - 0.3660  
  - 0.4050  
  - 0.2725  
  - 0.4034  
  - 0.3606  

- **Ortalama R² (Baseline CV):** **0.3615**

Bu değerler, baseline modelin genelleme başarısının sınırlı olduğunu göstermektedir.

---

## 3.6 Feature Engineering: Yeni Özelliklerin Oluşturulması

Notebook’ta, modelin açıklayıcılığını artırmak amacıyla üç önemli yeni feature türetilmiştir:

1. **price_per_km**  
   - Tanım: Fiyatın kilometreye göre normalize edilmiş hali  
   - Amaç: Aynı fiyat seviyesinde fakat farklı kilometreye sahip araçların göreli değerini yakalamak  
   - Formül:
     - `price_per_km = AskPrice_clean / (kmDriven_clean + 1)`

2. **log_kmDriven**  
   - Tanım: Kilometre değişkeninin log1p dönüşümü  
   - Amaç: Aşırı sağa çarpık dağılıma sahip kilometre değişkeninin daha dengeli bir dağılıma dönüştürülmesi

3. **log_price**  
   - Tanım: Fiyat değişkeninin log1p dönüşümü  
   - Amaç: Fiyat dağılımını normalize ederek modelin uç fiyat değerlerini daha iyi öğrenmesini sağlamak

Bu yeni değişkenler `df_fe` veri setine eklenmiş ve feature sayısı artırılmıştır. Notebook çıktısında `df_fe.head()` ile bu sütunların doğru şekilde oluştuğu görülmektedir.

---

## 3.7 Feature Engineering Sonrası Train / Validation / Test Ayrımı

Feature engineering uygulandıktan sonra veri seti üç parçaya ayrılmıştır:

- **Train set:** 10.433 satır, 12 feature  
- **Validation set:** 2.236 satır, 12 feature  
- **Test set:** 2.236 satır, 12 feature  

Notebook çıktısı:

```text
((10433, 12), (2236, 12), (2236, 12))
```

Bu yapı, özellikle **model optimizasyonu ve model seçimi** için daha sağlıklı bir değerlendirme ortamı sunmaktadır.

---

## 3.8 Feature Engineering Sonrası Cross-Validation (Validation CV)

Feature engineering sonrası model, güncellenen feature set ile tekrar 5 katlı K-Fold cross-validation’a tabi tutulmuştur. Notebook çıktısı:

```text
(array([0.490913  , 0.6197182 , 0.53152207, 0.60744894, 0.59299837]),
 0.5685201170122596)
```

Buna göre:

- Katman bazlı R² skorları:
  - 0.4909  
  - 0.6197  
  - 0.5315  
  - 0.6074  
  - 0.5930  

- **Ortalama R² (Feature Engineering CV):** **0.5685**

Bu sonuç, baseline CV ortalaması olan **0.3615** ile karşılaştırıldığında **belirgin bir iyileşme** olduğunu göstermektedir.

---

## 3.9 Feature Engineering Sonrası Validation Performansı

Feature engineering sonrası kurulan model, validation set üzerinde aşağıdaki metriklerle değerlendirilmiştir. Notebook çıktısı:

```text
(977805893637.6936, 988840.6816255557, 507941.6834246942, 0.5714288508799485)
```

Bu değerler:

- **MSE:** 977,805,893,637.69  
- **RMSE:** 988,840.68  
- **MAE:** 507,941.68  
- **R²:** 0.5714  

Base­line test R² değeri (**0.3660**) ile karşılaştırıldığında, feature engineering sonrası validation R² değerinin **0.57 seviyesine yükselmesi**, yeni feature’ların modele anlamlı katkı yaptığını açıkça göstermektedir.

---

## 3.10 Özet

- Temel değişkenler (Brand, model, Year, Age, kmDriven_clean, AskPrice_clean) kullanılarak başlangıç bir model kurulmuştur.  
- Baseline model test R² ≈ **0.37**, CV ortalama R² ≈ **0.36** seviyesindedir.  
- Feature engineering ile:
  - `price_per_km`, `log_kmDriven`, `log_price` gibi domain ve istatistiksel açıdan anlamlı üç yeni özellik eklenmiştir.  
  - Veri yapısı train/validation/test olarak 3’lü ayrılmış, toplam 12 feature ile model yeniden eğitilmiştir.  
  - CV ortalama R² değeri **0.36 → 0.57** seviyesine yükselmiştir.  
  - Validation üzerinde R² ≈ **0.57**, hata metriklerinde (RMSE, MAE) iyileşme sağlanmıştır.

Sonuç olarak, feature engineering aşaması modelin hem genelleme gücünü hem de açıklayıcılığını belirgin biçimde artırmış ve sonraki **model optimizasyon** adımı için güçlü bir temel oluşturmuştur.


