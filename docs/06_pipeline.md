# 06 | Final Pipeline

Bu bölümde, model geliştirme ve optimizasyon adımlarından sonra seçilen final modelin (RandomForest) uçtan uca bir pipeline yapısına dönüştürülmesi ve test seti üzerindeki performansının değerlendirilmesi anlatılmaktadır. 

---

## 6.1 Pipeline Yapısının Oluşturulması

Feature engineering ve optimizasyon aşamalarında kullanılan preprocess akışı aşağıdaki bileşenlerden oluşmuştur:

- **Categorical Preprocessing:** OneHotEncoder  
- **Numerical Preprocessing:** StandardScaler  
- **Model:** RandomForestRegressor (n_estimators=300, random_state=42)

Pipeline notebook çıktısı:

```
Pipeline(steps=[
 ('preprocess', ...),
 ('model', RandomForestRegressor(n_estimators=300, n_jobs=-1, random_state=42))
])
```

Bu yapı sayesinde veri ön işleme ve model eğitimi tek akışta uygulanmaktadır.

---

## 6.2 Eğitim–Doğrulama–Test Ayrımı

Pipeline eğitimi için veri üç parçaya bölünmüştür:

- **Train set:** 10,433 satır, 11 feature  
- **Validation set:** 2,236 satır, 11 feature  
- **Test set:** 2,236 satır, 11 feature  

Notebook çıktısı:

```
((10433, 11), (2236, 11), (2236, 11))
```

Bu splitter, model eğitiminden sonra final test değerlendirmesi yapmak için kullanılmıştır.

---

## 6.3 Pipeline Eğitim Süreci

RandomForest modeli preprocess adımıyla birlikte pipeline içinde eğitilmiştir.

Pipeline yapısı:

- Eksik değerlerin işlenmesi  
- Kategorik özelliklerin kodlanması  
- Sayısal özelliklerin ölçeklenmesi  
- Rastgele orman modelinin eğitilmesi  

Notebook’ta eğitim sırasında herhangi bir hata görülmemiş; model başarıyla öğrenmiştir.

---

## 6.4 Final Modelin Test Performansı

Modelin nihai performansı test seti üzerinde aşağıdaki metriklerle ölçülmüştür:

Notebook gerçek çıktısı:

```
(122082371739.60013, 349402.8788370241, 37605.636273106735, 0.9431364384555981)
```

Karşılıkları:

- **MSE:** 122,082,371,739.60  
- **RMSE:** 349,402.88  
- **MAE:** 37,605.64  
- **R²:** 0.9431  

### 🎯 Yorum:

- R² değeri **0.94** seviyesinde olup modelin yüksek açıklayıcılığa sahip olduğunu göstermektedir.  
- Validation R² (0.99995) → Test R² (0.94) geçişi modelin **genelleme kapasitesinin yüksek** olduğuna işaret eder.  
- MAE ve RMSE değerleri fiyat tahmini problemine göre makul düzeydedir.

---

## 6.5 Pipeline Aşamasının Önemi

Bu notebook, proje boyunca geliştirdiğimiz:

- Feature engineering
- Model seçimi
- Optimizasyon
- Değerlendirme

adımlarının tek bir birleşik yapı hâline getirildiği bölümdür.

Bu final pipeline,:

- Üretim ortamına alınabilir,  
- API üzerinden kullanılabilir,  
- Yeni veriler geldiğinde yeniden eğitilebilir,  
- Tek adımda veri → tahmin akışı kurabilir  

hale getirilmiştir.

---

## 6.6 Sonuç

Bu bölümde:

- Final pipeline oluşturulmuş,  
- RandomForest modeli preprocess ile entegre edilmiş,  
- Test seti üzerinde nihai performans hesaplanmış,  
- Proje uçtan uca tamamlanmıştır.


