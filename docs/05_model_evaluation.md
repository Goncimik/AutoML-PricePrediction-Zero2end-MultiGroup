# 05 | Model Evaluation

Bu bölümde, model optimizasyon aşamasından seçilen en iyi modelin performansı detaylı bir şekilde değerlendirilmiş; modelin tahmin gücü, hata metrikleri, feature importance analizi ve SHAP açıklamaları incelenmiştir. 
---

## 5.1 Veri Yükleme ve Ön Hazırlık

Bu notebook’ta model değerlendirmesi için:

- **X_train_full**
- **X_val**
- **y_train_full**
- **y_val**
- **final_model** (04. notebook’ta seçilen RandomForest modeli)

kullanılmıştır.

Veri yine aynı preprocess pipeline içinden geçirilmiş; model değerlendirme tüm feature engineering sonrası veri üzerinde yapılmıştır.

---

## 5.2 Final Modelin Performansı

Model, validation set üzerinde şu metriklerle değerlendirilmiştir:

- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
- **R² (Determination Coefficient)**

Bu metrikler 4. notebook’ta bulunan final sonuçlarla uyumlu olup, modelin yüksek doğruluk seviyesine sahip olduğunu göstermektedir.

Önceki notebook sonuçlarına göre:

- MSE ≈ 1.13 × 10⁸  
- RMSE ≈ 10,662  
- MAE ≈ 1,066  
- R² ≈ **0.99995**

Bu değerler RandomForest modelinin hem düşük hata hem yüksek doğruluk sağladığını doğrular.

---

## 5.3 Feature Importance Analizi

Modelin hangi değişkenlerden daha çok etkilendiğini görmek için `model.feature_importances_` değerleri incelenmiştir.

RandomForest'ın doğası gereği:

- **kmDriven_clean**
- **Year / Age**
- **Brand**
- **model**

gibi değişkenler yüksek önem puanı almıştır.

Bu analiz, modelin karar yapısının domain bilgisiyle uyumlu olduğunu göstermektedir.

---

## 5.4 SHAP Değerleri ile Model Açıklanabilirliği

Notebook’ta SHAP kütüphanesi kullanılarak modelin karar verme süreci açıklanmıştır.

Yapılan işlemler:

1. `shap.TreeExplainer(model)` ile açıklayıcı oluşturulmuştur.  
2. Validation set preprocess pipeline’dan geçirilmiştir.  
3. SHAP değerleri hesaplanmıştır:

```python
shap_values = explainer.shap_values(X_val_dense)
```

4. SHAP summary plot üretilmiştir (notebook çıktısında PNG olarak kayıtlıdır).

### SHAP Düşünceleri:

- SHAP grafiği modelin hangi feature’ları nasıl kullandığını net olarak göstermektedir.
- Özellikle:
  - **kmDriven_clean**,  
  - **Age**,  
  - **Brand**,  
  - **model**  
  gibi değişkenlerin tahminlere en büyük katkıyı yaptığı görülür.
- Kırmızı noktalar yüksek feature değerlerinin fiyatı nasıl artırdığını/azalttığını gösterir.

Bu grafik modelin hem açıklanabilir hem güvenilir olduğunu destekler.

---

## 5.5 Genel Değerlendirme

Bu notebook’taki analizlere göre:

- Seçilen final model olan **RandomForest**, validation set üzerinde **çok yüksek doğruluk** sunmaktadır.
- Feature importance ve SHAP analizleri:
  - Modelin domain bilgisiyle uyumlu kararlar verdiğini,
  - Tahminlerde kullanılan değişkenlerin etkisini,
  - Modelin kararlarına açıklık getiren içgörüleri sağlamaktadır.
- Model aşırı öğrenme göstermemiş; hem cross-validation hem validation setinde benzer başarıyı sürdürmüştür.

---

## 5.6 Sonuç

Model değerlendirme aşaması başarıyla tamamlanmış ve sonuç olarak:

- Model performansı güçlüdür,
- Karar mekanizması açıklanabilirdir,
- Feature engineering sonrası oluşturulan özelliklerin modele etkisi nettir,
- RandomForest modeli final pipeline için uygun bulunmuştur.

Bu bölüm, pipeline oluşturma aşamasına geçmeden önce modelin güvenilirliğini ve doğruluk seviyesini teyit eden kritik adımdır.

