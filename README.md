# BLM101 – Bilgisayar Mühendisliğine Giriş Dersi Dönem Projesi

Adı Soyadı: Aliekber Görmüş
Öğrenci Numarası: 24360859061
Proje Konusu: Veri Depolama ve RLE Sıkıştırma Algoritması

🎥 Proje Sunum Videosu:
Proje anlatım videoma aşağıdaki linkten ulaşabilirsiniz:
https://youtu.be/xEjGy8B7Pvs

📝 Proje Açıklaması:
## 🛠 Kodun Çalışma Mantığı

Bu proje, temel veri sıkıştırma yöntemlerinden biri olan **Run-Length Encoding (RLE)** algoritmasını Python dili ile simüle eder. Programın temel çalışma prensipleri aşağıdadır:

### 1. Sıkıştırma (Encode) Algoritması
`rle_encode` fonksiyonu, ham veriyi (örneğin: `AAAAABBB`) alır ve şu adımları izler:
- Veri üzerinde bir döngü (for loop) ile baştan sona ilerler.
- Her adımda, o anki karakterin bir önceki karakterle **aynı olup olmadığını** kontrol eder.
- Eğer karakterler aynıysa, bir sayaç değişkenini (`sayac`) artırır.
- Eğer karakter değişirse; o ana kadar sayılan değeri ve karakteri sonuç değişkenine ekler (Örn: `5A`), sayacı sıfırlar ve yeni karakteri saymaya başlar.
- **Not:** Döngü bittiğinde son kalan karakter grubunu da kaybetmemek için döngü dışında son bir ekleme işlemi daha yapar.

### 2. Geri Çözme (Decode) Algoritması
`rle_decode` fonksiyonu, sıkıştırılmış veriyi (örneğin: `12A3B`) alıp orijinal haline döndürür. Bu fonksiyonun önemli bir özelliği **çok basamaklı sayıları** da desteklemesidir:
- Veriyi okurken karşılaştığı karakterin sayı olup olmadığını (`isdigit()`) kontrol eder.
- Eğer sayı ise (örneğin `12`), bunu basamak basamak okuyarak tam sayı değerini elde eder.
- Sayıdan hemen sonra gelen karakteri tespit eder ve Python'un string çarpma özelliği (`karakter * adet`) ile o karakteri tekrar oluşturur.

### 3. Sıkıştırma Oranı Hesabı
Program, sıkıştırma işleminin ne kadar verimli olduğunu kullanıcıya göstermek için matematiksel bir hesaplama yapar:
- **Formül:** `(1 - (Sıkıştırılmış Boyut / Orijinal Boyut)) * 100`
- Bu işlem sonucunda verinin boyutunun yüzde kaç oranında küçüldüğü hesaplanır ve virgülden sonra 2 basamak olacak şekilde ekrana yazdırılır.

### 4. Kullanıcı Arayüzü
Program, `while True` döngüsü içinde çalışan interaktif bir menü sunar. Kullanıcı `1`, `2` veya `3` tuşlarına basarak sıkıştırma, çözme veya çıkış işlemlerini gerçekleştirebilir.
