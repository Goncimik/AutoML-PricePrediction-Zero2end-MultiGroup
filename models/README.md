# Model Dosyaları

Bu klasör, proje kapsamında üretilen makine öğrenimi model dosyalarının (ör. `.pkl`) tutulması için oluşturulmuştur.  
Ancak nihai model dosyası GitHub’ın dosya boyutu sınırı (100 MB) nedeniyle bu repoya eklenmemiştir.

##  Nihai Model Bilgileri

- **Dosya adı:** `final_car_price_model.pkl`  
- **Boyut:** ~185 MB  
- **GitHub’a eklenmeme nedeni:** GitHub'ın tek dosya için maksimum 100 MB limiti bulunmaktadır.  
- **Modelin konumu:**  
  - Geliştirici bilgisayarında (lokalde)  
  - Kaggle notebook çıktılarında yeniden üretilebilir durumda  

##  Modelin Nasıl Yeniden Üretileceği

Aşağıdaki notebook’lar çalıştırılarak aynı final model dosyası tekrar oluşturulabilir:

- `notebooks/06_pipeline.ipynb`
- `notebooks/07_final_model.ipynb`

Bu notebook’lar model eğitim sürecini uçtan uca içermektedir. Çalıştırıldığında model, çalışma dizinine `final_car_price_model.pkl` olarak kaydedilir.

##  Not

Gerçek projelerde büyük model dosyalarının versiyon kontrol sistemlerine eklenmemesi yaygın ve tavsiye edilen bir pratiktir.  
Bu nedenle model dosyası repoda değildir; ancak istenildiğinde kolayca yeniden üretilebilir.

