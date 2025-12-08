# 07 | Final Model 

Bu bölüm, `final-model.ipynb` notebook’unda gerçekleştirilen **uçtan uca final model sürecini**, kullanılan **modelleri**, **veri sızıntısı (data leakage) tespitini**, **düzeltilmiş feature set ile elde edilen sonuçları** ve **son rastgele orman (RandomForest) modelinin test performansını** özetler.

---

## 7.1 Genel Akış

Final notebook şu aşamaları tek dosya içinde birleştirir:

1. EDA özet adımları (1–10 arası başlıklar)  
2. Baseline model ve ilk performans  
3. Feature engineering (price_per_km, log_kmDriven, log_price vb.)  
4. RandomForest, XGBoost, LightGBM karşılaştırması  
5. **Data leakage tespiti ve log_price kolonunun kaldırılması**  
6. Leakage düzeltilmiş feature set ile modellerin yeniden eğitilmesi  
7. En iyi modelin (RandomForest) seçilmesi  
8. Final modelin train+validation verisiyle yeniden eğitilmesi  
9. Test setinde gerçek performansın ölçülmesi  
10. Feature importance ve SHAP ile model açıklanabilirliği  
11. Kaydedilmiş model dosyası ve tahmin fonksiyonu (`predict_car_price`)

---

## 7.2 İlk Model Karşılaştırması (Leakage Varken)

Feature engineering sonrası, **log_price** değişkeni feature set içinde iken üç model eğitilmiş ve validation setinde karşılaştırılmıştır:

- RandomForest  
- XGBoost  
- LightGBM  

Notebook’taki ilk sonuç tablosu:

```text
          Model           MSE           RMSE           MAE        R2
0  RandomForest  1.136894e+08   10662.522984   1066.425493  0.999950
1       XGBoost  9.342390e+09   96656.041188  21257.610582  0.995905
2      LightGBM  3.332650e+10  182555.479344  18817.423581  0.985393
```

Bu tabloda:

- RandomForest için **R² ≈ 0.99995** gibi “aşırı iyi” bir skor görülmektedir.  
- Hatalar (RMSE, MAE) çok düşük, R² ise neredeyse 1’e yakındır.

Notebook’ta bu sonuç **“Validation sonuçlarının aşırı yüksek görünmesi”** ile ilişkilendirilmiş ve bunun sebebi olarak **hedef sızıntısı (data leakage)** tespit edilmiştir.

---

## 7.3 Data Leakage Tespiti ve log_price’ın Kaldırılması

İnceleme sonucunda:

- `log_price` değişkeninin, hedef değişken `AskPrice_clean` ile **doğrudan ilişkili** olduğu (hatta türevi olduğu)  
- Bu nedenle `log_price`’ın modele feature olarak eklenmesinin, modelin hedefi “önceden bilmesine” benzer bir etki yarattığı,  
- Bu durumun, validation performansını gerçekçi olmayan şekilde şişirdiği

tespit edilmiştir.

Bu nedenle final model sürecinde:

- `log_price` kolonu tamamen **feature setten çıkarılmış**,  
- Sadece **orijinal bilgilerden ve güvenli türetilmiş değişkenlerden** oluşan bir feature set kullanılmıştır.

Notebook kodunda:

```python
# 1) log_price kolonunu kaldırıyoruz
df_fe_fixed = df_fe.drop(columns=["log_price"])
```

---

## 7.4 Düzeltilmiş Feature Set

Leakage düzeltildikten sonra aşağıdaki feature set kullanılmıştır:

- **Kategorik (cat_cols_fix):**
  - Brand  
  - model  
  - Transmission  
  - Owner  
  - FuelType  

- **Sayısal (num_cols_fix):**
  - Year  
  - Age  
  - kmDriven_clean  
  - price_per_km  
  - km_per_year  
  - log_kmDriven  

Böylece model:

- Hem **domain bilgisine dayalı** (price_per_km, km_per_year),  
- Hem de **istatistiksel dönüşümlere dayalı** (log_kmDriven),  
- Aynı zamanda marka/model bilgilerini içeren  
zengin bir feature set ile eğitilmiştir.

Veri, bu feature set ile tekrar **Train / Validation / Test** olarak bölünmüştür:

```text
((10433, 11), (2236, 11), (2236, 11))
```

Yani:

- Train: 10.433 satır, 11 feature  
- Validation: 2.236 satır, 11 feature  
- Test: 2.236 satır, 11 feature  

(11 feature = 5 kategorik + 6 sayısal sütun)

---

## 7.5 Leakage Düzeltilmiş Modellerin Validation Performansı

Aynı üç model (RandomForest, XGBoost, LightGBM) leakage düzeltilmiş feature set ile **validasyon setinde tekrar eğitilmiş ve karşılaştırılmıştır.**

Notebook çıktısı:

```text
          Model           MSE           RMSE           MAE        R2
0  RandomForest  5.223972e+10  228560.094034  32638.695173  0.977103
1       XGBoost  6.673276e+10  258326.842825  62908.211756  0.970751
2      LightGBM  1.096227e+11  331093.177280  66921.540137  0.951953
```

Model bazında:

- **RandomForest:**
  - MSE  ≈ 5.22 × 10¹⁰  
  - RMSE ≈ 228,560.09  
  - MAE  ≈ 32,638.70  
  - R²   ≈ **0.9771**

- **XGBoost:**
  - MSE  ≈ 6.67 × 10¹⁰  
  - RMSE ≈ 258,326.84  
  - MAE  ≈ 62,908.21  
  - R²   ≈ 0.9708  

- **LightGBM:**
  - MSE  ≈ 1.10 × 10¹¹  
  - RMSE ≈ 331,093.18  
  - MAE  ≈ 66,921.54  
  - R²   ≈ 0.9520  

Buradan:

- Hata metrikleri ve R² açısından **en iyi validation performansı RandomForest modelindedir.**  
- XGBoost ve LightGBM de iyi performans vermiş olsa da, RandomForest hem **daha düşük hata**, hem de **daha yüksek R²** ile öne çıkmıştır.

---

## 7.6 Final Model Seçimi

Notebook’ta bu sonuçlar yorumlanırken:

> **“En iyi validation performansı: RandomForest (R2 ≈ 0.977)”**

şeklinde ifade edilmiş ve final model olarak:

- **RandomForestRegressor (leakage düzeltilmiş feature set ile)**

seçilmiştir.

Bu aşamadan sonra RandomForest:

- Train + Validation verisinin birleştirilmiş hâli üzerinde tekrar eğitilmiş,  
- Ayrı tutulmuş Test seti üzerinde değerlendirilmiştir.

---

## 7.7 Final Modelin Test Performansı

RandomForest modelinin **Train+Validation üzerinde yeniden eğitildikten sonra** test seti üzerindeki gerçek performansı notebook’ta şu şekilde raporlanmıştır:

```text
(119397886714.74586, 345539.992930986, 34141.784841979716, 0.9443868186476821)
```

Bu değerler:

- **MSE:** 119,397,886,714.75  
- **RMSE:** 345,539.99  
- **MAE:** 34,141.78  
- **R²:** 0.9444  

### Yorumlar:

- Validation R² ≈ 0.9771 → Test R² ≈ 0.9444  
  - Performans **bir miktar düşmüş olsa da**, hala **çok yüksek** bir açıklama gücü bulunmaktadır.  
  - Bu fark, validation ve test setlerindeki dağılım farklarından ve veri yapısından kaynaklanabilir.
- MAE ≈ 34K → Ortalama tahmin hatası bu seviyededir; kullanılan fiyat aralığıyla birlikte değerlendirildiğinde **kabul edilebilir** bir hata düzeyidir.  
- RMSE ≈ 345K → Büyük hataların (outlier fiyatların) modele olan etkisini yansıtır.

Sonuç:  
**RandomForest modeli, leakage düzeltilmiş feature set ile hem validation hem de test setinde güçlü bir genel performans sergilemiştir.**

---

## 7.8 Feature Importance Analizi (Final RandomForest)

Final RandomForest modeli için `feature_importances_` değerleri çıkarılmış ve en önemli feature’lar incelenmiştir.

Notebook’taki önem tablosu (ilk satırlar):

```text
                     Feature  Importance
475             price_per_km    0.565477
474           kmDriven_clean    0.086508
477             log_kmDriven    0.085271
190            model_G Class    0.044914
304  model_Phantom Series II    0.034033
20          Brand_Land Rover    0.017058
26       Brand_Mercedes-Benz    0.015942
31             Brand_Porsche    0.015868
19         Brand_Lamborghini    0.014946
3                  Brand_BMW    0.014434
400               model_Urus    0.013132
```

Buna göre:

- **En önemli değişken:**  
  - `price_per_km` (importance ≈ 0.565)  
  → Fiyat / km oranı, aracın piyasa değerini açıklamada en kritik feature.

- Diğer güçlü etkiler:
  - `kmDriven_clean`  
  - `log_kmDriven`  
  - Lüks marka ve model dummy’leri:
    - `model_G Class`
    - `model_Phantom Series II`
    - `Brand_Land Rover`
    - `Brand_Mercedes-Benz`
    - `Brand_Porsche`
    - `Brand_Lamborghini`
    - `Brand_BMW`
    - `model_Urus`

Bu sonuçlar:

- Hem domain bilgisine (km, fiyat, marka değeri),  
- Hem de modelin yakaladığı karmaşık ilişkilerin lüks segment araçlarda yoğunlaştığına

işaret etmektedir.

---

## 7.9 Kaydedilen Model ve Tahmin Fonksiyonu

Final notebook’ta, eğitilen model **pickle** ile dışarı kaydedilmiş ve daha sonra tekrar yüklenerek bir tahmin fonksiyonu tanımlanmıştır:

- Kaydedilen dosya adı:  
  - `final_car_price_model.pkl`

- Yükleme adımı:
  - `loaded_model = pickle.load(f)`

- Tahmin fonksiyonu:

```python
def predict_car_price(input_dict):
    """
    input_dict: Kullanıcının girdiği araç özelliklerini içeren sözlük
    Örnek: {"Brand": "...", "model": "...", "Year": 2018, "kmDriven_clean": 45000, ...}
    """
    # dict -> DataFrame -> pipeline.predict -> fiyat tahmini
```

Notebook’ta fonksiyon test edildiğinde örnek bir tahmin çıktısı:

```text
94579.18666666666
```

Bu, verilen örnek araç özelliklerine göre tahmin edilen fiyatın yaklaşık **94,579** birim olduğunu göstermektedir.

---

## 7.10 Özet

`final-model.ipynb` notebook’una göre:

- EDA, baseline, feature engineering, model karşılaştırma, leakage tespiti ve düzeltme adımları **tek bir uçtan uca akışta** birleştirilmiştir.
- Önce log_price kaynaklı data leakage tespit edilmiş, ardından bu feature setten çıkarılmıştır.
- Leakage düzeltilmiş feature set üzerinde **RandomForest, XGBoost, LightGBM** tekrar karşılaştırılmış; en iyi model **RandomForest** olmuştur:
  - Validation R² ≈ **0.977**  
  - Test R² ≈ **0.944**
- Feature importance ve SHAP analizleri, modelin karar mekanizmasını **açıklanabilir** kılmaktadır.
- Final model pickle ile kaydedilmiş ve `predict_car_price` fonksiyonu ile **üretim ortamına hazır** bir tahmin arayüzü tanımlanmıştır.

Bu doküman, final notebook’un uçtan uca tüm kritik adımlarını, kullanılan modelleri ve elde edilen performans değerlerini özetleyen son parçadır.

