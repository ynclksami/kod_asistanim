# ==============================================================================
# KOD-ASİSTAN PROJESİ - SONSUZ DÖNGÜ KAPANI VE GEOMETRİK FRAKTAL SANATI
# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / Turtle Grafik ve Sınır Kontrollü While Döngüsü
# ==============================================================================

import turtle

print("=== KOD-ASİSTAN: DİJİTAL SANAT MOTORU AKTİF ===")

# a) ve c) Kullanıcıdan dinamik eksen/açı verisinin alınması
try:
    eksen_sayisi = int(input("Çizilmesini istediğiniz fraktal eksen sayısını giriniz (Örn: 4, 6, 8): "))
    if eksen_sayisi <= 0:
        print("Hata: Eksen sayısı sıfır veya negatif olamaz! Varsayılan olarak 6 atanıyor.")
        eksen_sayisi = 6
except ValueError:
    print("Geçersiz giriş! Varsayılan eksen sayısı 6 olarak ayarlandı.")
    eksen_sayisi = 6

# Matematiksel dönüş açısı formülü
aci = 360 / eksen_sayisi
print(f"Hesaplanan Dönüş Açısı: {aci:.1f} Derece.")
print("Grafik motoru tetikleniyor, lütfen açılan pencereyi izleyiniz...\n")

# Çizim kalemi ve pencere ayarları
asistan_kalem = turtle.Turtle()
turtle.bgcolor("black")          # Estetik dijital sanat arka planı
asistan_kalem.pencolor("cyan")   # Canlı turkuaz çizgi rengi
asistan_kalem.pensize(2)
asistan_kalem.speed(0)           # En yüksek çizim hızı

# ç) Çizgilerin her adımda büyümesini sağlayacak sayacın tanımlanması
cizgi_boyu = 0

# d) while True ile sonsuz döngü motorunun başlatılması
while True:
    # e) Kaplumbağanın hareket ettirilmesi ve boyun artırılması
    asistan_kalem.forward(cizgi_boyu)
    asistan_kalem.left(aci)
    
    cizgi_boyu += 2  # Her turun sonunda çizgi boyunu 2 piksel artırarak spiral etki yaratma

    # f) Güvenlik Sınırı ve Break Kontrolü (Sonsuz Döngü Kapanı)
    if cizgi_boyu >= 300:
        print(f"Program Güvenliği Sağlandı: 300 piksel sınırında sonsuz döngü kırıldı. (Mevcut Boy: {cizgi_boyu}px)")
        break

# g) Çizim bittiğinde ekranın açık kalmasını sağlayan komut
turtle.done()