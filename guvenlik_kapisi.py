print("=== KOD-ASİSTAN: AKILLI GÜVENLİK KAPISI SİSTEMİ ===")

# Kullanıcıdan rol ve güvenlik derecesi bilgilerini dinamik olarak alma
# .lower() metodu ile büyük-küçük harf duyarlılığı hatasını önlemek için veri standardizasyonu sağlanır
rol = input("Lütfen rolünüzü küçük harfle giriniz (Yönetici/Personel): ").strip().lower()

# Eğer rol yönetici ise güvenlik derecesine bakılmaksızın geçiş verilir
if rol == "yönetici":
    print("\nErişim izni verildi. Hoş Geldiniz Sayın Yönetici.")

# Eğer rol personel ise iç içe kontrol ile güvenlik derecesi sorgulanır
elif rol == "personel":
    # Tip dönüşümü tuzağına düşmemek için input float veya int ile sayıya dönüştürülür
    guvenlik_derecesi = int(input("Lütfen güvenlik derecenizi giriniz (Sayısal): "))
    
    if guvenlik_derecesi >= 3:
        print("\nErişim izni verildi. Laboratuvar alanına geçebilirsiniz.")
    else:
        print("\nErişim engellendi. Yetersiz güvenlik derecesi!")

# Tanımlanan roller dışında bir veri girilirse
else:
    print("\nHatalı rol tanımlaması! Güvenlik protokolü devreye girdi.")