# 04 | Model Optimization

Bu bölümde, üçüncü notebook’ta oluşturulan feature engineering sonrası veri seti kullanılarak farklı modellerin denenmesi ve validation performanslarının karşılaştırılması anlatılmaktadır.

---

## 4.1 RandomForest, XGBoost ve LightGBM Modellerinin Kurulması

Bu aşamada feature engineering sonrası elde edilen veri seti üzerinde üç farklı model kurulmuştur:

- **RandomForestRegressor**
- **XGBoostRegressor**
- **LightGBMRegressor**

Tüm modeller aynı train–validation ayrımı üzerinde eğitilmiş ve karşılaştırılmıştır.  
Veri seti; daha önceki notebook’ta oluşturulan:

- Train set (X_train_full, y_train_full)
- Validation set (X_val, y_val)

kümeleri kullanılarak modellenmiştir.

Her model için:

- Aynı feature set
- Aynı ön işleme (OneHotEncoder + sayısal kolonlar)
- Aynı değerlendirme metrikleri

kullanılmıştır.

---

## 4.2 Modellerin Validation Set Üzerinde Karşılaştırılması

Notebook’ta, her model için validation set üzerinde şu metrikler hesaplanmıştır:

- **MSE** (Mean Squared Error)
- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **R²** (Determination Coefficient)

Gerçek notebook çıktısı aşağıdaki gibidir:

```text
          Model           MSE           RMSE           MAE        R2
0  RandomForest  1.136894e+08   10662.522984   1066.425493  0.999950
1       XGBoost  9.342390e+09   96656.041188  21257.610582  0.995905
2      LightGBM  3.332650e+10  182555.479344  18817.423581  0.985393
```

Bu tabloya göre:

- **RandomForest**:
  - MSE  ≈ 1.13 × 10⁸  
  - RMSE ≈ 10.662  
  - MAE  ≈ 1.066  
  - R²   ≈ **0.99995**

- **XGBoost**:
  - MSE  ≈ 9.34 × 10⁹  
  - RMSE ≈ 96.656  
  - MAE  ≈ 21.258  
  - R²   ≈ 0.99591

- **LightGBM**:
  - MSE  ≈ 3.33 × 10¹⁰  
  - RMSE ≈ 182.555  
  - MAE  ≈ 18.817  
  - R²   ≈ 0.98539

---

## 4.3 En İyi Modelin Seçilmesi

Validation performans karşılaştırması sonucunda:

- **En yüksek R²**: RandomForest (**0.99995**)  
- **En düşük MSE, RMSE ve MAE**: RandomForest  
- XGBoost ve LightGBM iyi performans gösterseler de hem hata metriklerinde hem de R² değerinde RandomForest’ın gerisinde kalmıştır.

Bu nedenle:

> **Bu notebook’a göre en iyi model: _RandomForestRegressor_ olarak seçilmiştir.**

RandomForest, hem yüksek doğruluk hem de kararlı tahmin performansı ile final pipeline için en güçlü aday olarak belirlenmiştir.

---

## 4.4 Model Optimization Özet Bulgular

`4-model-optimization.ipynb` notebook'u özetle şunları göstermektedir:

- Feature engineering sonrası aynı veri seti üzerinde **RandomForest, XGBoost ve LightGBM** karşılaştırılmıştır.
- Validation setinde:
  - RandomForest, R² ≈ **0.99995** ile belirgin şekilde en iyi performansı vermiştir.
  - XGBoost ve LightGBM de yüksek performans göstermiş ancak RandomForest’ın gerisinde kalmıştır.


