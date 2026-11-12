print("=== KOD-ASİSTAN AKTİF ÇALIŞMA ORTAMI BAŞLATILDI ===")
# AKTİF DÖNGÜ MOTORU
# Koşul True olduğu sürece program açıkça çıkış istenene kadar kapanmaz.
while True:
    print("\n--- ANA MENÜ ---")
    print("1 - Sepet ve İndirim Hesaplama Katmanı")
    print("2 - Sistem Durum Raporunu Görüntüle")
    print("3 - Güvenli Çıkış")
    print("----------------")
    secim = input("Lütfen yapmak istediğiniz işlemin numarasını giriniz (1/2/3): ") .strip()
    # ÇOK KRİTERLİ DALLANMA VE DÖNGÜ KONTROL ALANI
    if secim == "1":
        print("\n[MODÜL TETİKLENDİ: Sepet Hesaplama]")
        tutar = float(input("Sepet tutarını giriniz (TL): "))
        if tutar > 500:
            print(f"%10 İndirim Uygulandı! Ödenecek Tutar: {tutar * 0.90:.2f} TL")
        else:
            print(f"Net Ödenecek Tutar: {tutar:.2f} TL")
    elif secim == "2":
        print("\n[MODÜL TETİKLENDİ: Örnek Sistem Durumu Raporu]")
        print("Mevcut Sürüm: Kod-Asistan v0.3")
        print("Bellek Durumu: RAM Kararlı | Çekirdek Motor: Aktif")
        print("Depo Entegrasyonu: Bulut Deposu Bağlantısı Hazır.")
    elif secim == "3":
        print("\nGüvenli çıkış protokolü devreye girdi.")
        print("Güvenli günler dileriz!")
        # KONTROL İFADESİ: Döngü burada tamamen kırılır ve program sonlanır.
        break
    else:
        # Kararsız veri girişlerinin yönetilmesi (Hata Engelleyici Katman)
        print("\nHatalı Seçim! Girdiğiniz değer menü standartlarına uymuyor.")
        print("Lütfen yalnızca 1, 2 veya 3 değerlerinden birini giriniz.")
print("\n=== PROGRAM BAŞARIYLA KAPATILDI ===")
