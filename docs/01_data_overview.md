# 01 | Data Overview (EDA)

Bu bölüm, ikinci el araç fiyat tahmini projesinde kullanılan veri setinin genel yapısını, temel özelliklerini ve keşifsel veri analizi bulgularını özetlemektedir. Tüm bu analizler `1-eda.ipynb` notebook’u üzerinden gerçekleştirilmiştir.

---

## 1. Veri Setinin Genel Tanımı

🔗 Kaggle Veri Seti Adı:

“Used Cars Price Prediction Dataset” (used_cars_dataset_v2.csv)

🔗 Kaggle Linki:

https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset

Çalışmada kullanılan veri seti, ikinci el araçların çeşitli özelliklerini içeren tabular bir yapıya sahiptir. Temel değişkenler:

- **Make / Model**: Araç marka–model bilgisi  
- **Year**: Üretim yılı  
- **kmDriven**: Kullanım kilometresi  
- **Fuel Type**: Benzin, Dizel vb.  
- **Transmission**: Manual / Automatic  
- **Owner Type**: 1., 2. veya daha fazla sahiplik  
- **AskPrice**: Satıcının istediği fiyat (hedef değişken)

Toplam gözlem sayısı ~15.000 civarındadır.

---

## 2. Veri Temizliği

Notebook’ta yapılan temel veri temizleme adımları şunlardır:

- **kmDriven** ve **AskPrice** alanlarında görülen hatalı veya uç değerler incelenmiş, gerekli düzeltmeler yapılmıştır.  
- Kategorik değişkenlerde görülen yazım hataları giderilmiş, sınıflar standardize edilmiştir.  
- Sayısal olmayan fakat sayısal yorum gerektiren değişkenler uygun dönüşümlerle modele hazır hale getirilmiştir.

---

## 3. Sayısal Değişken Analizleri

EDA sürecinde aşağıdaki sayısal değişkenlerin dağılımları incelenmiştir:

- Üretim yılı dağılımı  
- Araçların kilometre kullanım dağılımı  
- Fiyat dağılımı  

Genel bulgular:

- Kilometre değerleri sağa çarpık bir dağılım göstermektedir.  
- Fiyat değişkeni geniş bir aralıkta dağılmış olup log-transform veya ölçeklendirme ihtiyacı olduğu gözlemlenmiştir.  
- Daha yeni araçların ortalama fiyatları belirgin şekilde daha yüksektir.

---

## 4. Korelasyon Analizi

Sayısal değişkenler arasında korelasyon matrisi incelenmiştir.

Öne çıkan ilişkiler:

- **Year ↗ AskPrice** → Yeni araçlar daha pahalı.  
- **kmDriven ↘ AskPrice** → Çok kullanılan araçların fiyatı düşüyor.  

Korelasyon düzeyleri modelleme aşaması için anlamlı içgörüler sunmaktadır.

---

## 5. Kategorik Değişkenler ve Fiyat İlişkisi

Kategorik değişkenlerin fiyat üzerindeki etkisi grafiksel olarak incelenmiştir:

- **Fuel Type:** Dizel araçların ortalama fiyatı biraz daha yüksektir.  
- **Transmission:** Otomatik vitesli araçlar genellikle daha pahalıdır.  
- **Owner Type:** Tek sahipli araçların fiyatı daha yüksek eğilim göstermektedir.

---

## 6. EDA Özet Bulgular

- Veri seti temiz, modellemeye uygun yapıdadır.  
- Fiyat değişkeni ciddi varyansa ve aykırı değerlere sahiptir; ölçekleme ve dönüşüm yöntemleri gereklidir.  
- Kilometre, üretim yılı gibi temel değişkenler fiyatı belirlemede kritik rol oynamaktadır.  
- Kategorik değişkenlerin de fiyat üzerinde anlamlı etkileri gözlemlenmiştir.  
- EDA sonucunda ortaya çıkan içgörüler, baseline model ve feature engineering aşamalarına yön vermektedir.

---

Bu doküman, veri setinin ilk analiz aşamasını özetlemekte ve sonraki modelleme süreçleri için temel sağlamaktadır.
