# BLM101 - Bilgisayar Muhendisligine Giris Dersi Donem Projesi
# Ogrenci: Aliekber Gormus
# Konu: RLE (Run-Length Encoding) Sikistirma Algoritmasi

def rle_encode(veri):
    """
    Bu fonksiyon, girilen ham veriyi (ornegin 'AAAAA') RLE algoritmasi ile
    sikistirilmis hale (ornegin '5A') donusturur.
    """
    if not veri:
        return "" 

    sikismis_veri = ""
    sayac = 1

    # Veri uzerindeki her karakteri kontrol et
    for i in range(1, len(veri)):
        if veri[i] == veri[i - 1]:
            # Eger karakter bir oncekiyle ayniysa sayaci artir
            sayac += 1
        else:
            # Karakter degistiyse, sayaci ve karakteri sonuca ekle
            sikismis_veri += str(sayac) + veri[i - 1]
            sayac = 1 # Sayaci sifirla

    # Dongu bittiginde son kalan grubu da ekle
    sikismis_veri += str(sayac) + veri[-1]
    
    return sikismis_veri

def rle_decode(sikismis_veri):
    """
    Bu fonksiyon, sikistirilmis veriyi (ornegin '5A') alir ve
    orijinal haline (ornegin 'AAAAA') geri dondurur.
    """
    orijinal_veri = ""
    i = 0
    
    while i < len(sikismis_veri):
        adet_str = ""
        # Sayisal degeri bul (Orn: '12'A icin 1 ve 2'yi al)
        while i < len(sikismis_veri) and sikismis_veri[i].isdigit():
            adet_str += sikismis_veri[i]
            i += 1
            
        if adet_str:
            adet = int(adet_str)
            # Sayidan sonra gelen karakteri al
            karakter = sikismis_veri[i]
            # Karakteri adet kadar cogaltip ekle
            orijinal_veri += karakter * adet
            i += 1
            
    return orijinal_veri

def oran_hesapla(orijinal, sikismis):
    """
    Sikistirma basarisini yuzde (%) olarak hesaplar.
    """
    if len(orijinal) == 0:
        return 0
    
    oran = (1 - (len(sikismis) / len(orijinal))) * 100
    return oran

# --- Ana Program Blogu ---
if __name__ == "__main__":
    print("--- RLE Sikistirma Programina Hos Geldiniz ---")
    
    while True:
        print("\nLutfen bir islem seciniz:")
        print("1. Sikistirma (Encode)")
        print("2. Cozme (Decode)")
        print("3. Cikis")
        
        secim = input("Seciminiz (1/2/3): ")
        
        if secim == '1':
            girilen_veri = input("\nSikistirilacak metni girin (Orn: AAAAABBB): ")
            sonuc = rle_encode(girilen_veri)
            print(f"-> Sikistirilmis Veri: {sonuc}")
            
            # Sikistirma oranini goster
            basari = oran_hesapla(girilen_veri, sonuc)
            print(f"-> Sikistirma Orani: %{basari:.2f}")
            print(f"-> (Orijinal Boyut: {len(girilen_veri)}, Yeni Boyut: {len(sonuc)})")
            
        elif secim == '2':
            girilen_veri = input("\nCozulecek kodu girin (Orn: 5A3B): ")
            try:
                sonuc = rle_decode(girilen_veri)
                print(f"-> Orijinal Veri: {sonuc}")
            except:
                print("Hata: Girdiginiz format cozulemedi! Lutfen '3A2B' formatinda girin.")
                
        elif secim == '3':
            print("Programdan cikiliyor...")
            break
        else:
            print("Gecersiz secim, lutfen tekrar deneyin.")
