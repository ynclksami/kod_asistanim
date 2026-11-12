# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / İç İçe for Döngüleri ve Grafiksel Matris Yönetimi
import turtle
print("=== KOD-ASİSTAN: AKTİF DÖNDÜRÜLMÜŞ ÜÇGEN DESENİ ===")
print("Grafik penceresi açılıyor, iç içe döngülerin mekanizmasını izleyiniz...\n")
# Çizim aracının hazırlanması ve kararlı grafik ayarları
asistan_kalem = turtle.Turtle()
asistan_kalem.speed(0) # Çizimi hızlandırmak için en yüksek hız (0) modu
asistan_kalem.pencolor("blue") # Mavi tasarım rengi
asistan_kalem.pensize(2)
# ==============================================================
# MANTIKSAL HİYERARŞİ: İÇ İÇE DÖNGÜ MOTORU
# ==============================================================
# 1. DIŞ DÖNGÜ: Toplam şekil adedini ve dönüş eksenini yönetir.
# Bu döngü 36 kez dönecek, yani ekranda 36 adet geometrik şekil oluşacaktır.
for dis_sira in range(36):
# 2. İÇ DÖNGÜ: Temel geometrik şekli (Eşkenar Üçgen) çizer.
# Dış döngünün HER BİR TURUNDA bu iç döngü 3 turunu tamamen bitirir.
    for ic_sira in range(4): #range 3 iken 4 yapıldı
        asistan_kalem.forward(120) # 120 piksel ileri git
        asistan_kalem.left(90) # Eşkenar üçgen dış açısı (120 derece) sola dön. 120 iken 90 yapıldı.
        # İÇ DÖNGÜNÜN BİTİŞ ALANI
    # Bir adet üçgen çizimi bitti! Şimdi dış döngünün kontrolündeyiz.
    # Bir sonraki üçgenin bir öncekinin üstüne binmemesi için ekseni 10 derece kaydırıyoruz.
    asistan_kalem.right(10)
    #Alttaki 4 satır sonra eklendi
    if dis_sira % 2 == 0:
        asistan_kalem.pencolor("purple")
    else:
        asistan_kalem.pencolor("blue")
print("Algoritma Tamamlandı: 36 adet üçgen, iç içe döngü mimarisiyle işlendi.")
turtle.done()