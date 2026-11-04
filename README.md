Proje Yazarı: Sami YENCİLEK
# Projenin Adı: Kod-Asistan v0.1
## Projenin Amacı: Kullanıcılara günlük işlerinde (hesaplama, selamlama vb.) yardımcı olacak bir dijital asistan tasarlamak
## Projenin Hedefleri: Bu asistanın ilerleyen zamanlarda hangi özellikleri kazanacağını (örneğin v1.0 Akıllı Menü, v2.0 Veri Saklama)
## Projenin Kapsamı

Bu proje kapsamında, akıllı baraj otomasyonunda su seviyesini saatlik olarak takip eden bir döngü mekanizması modellenmiştir. Sistemde başlangıç saati 1 olarak belirlenir. Her saat sensörden alınan su seviyesi kontrol edilir.

Su seviyesi 50 metreyi aşmadığı sürece baraj kapakları kapalı tutulur ve saat sayacı bir artırılır. Su seviyesi 50 metreyi aştığında döngü sonlandırılır. Ardından tahliyenin gerçekleştiği saat ve kritik su seviyesi ekrana yazdırılır.

**KRİTİK EŞİK Sözde Kodu:**

1. Saat değişkenini 1 olarak başlat.
2. Su seviyesini sensörden oku.
3. Su seviyesi 50 metreden büyük mü kontrol et.
4. Eğer su seviyesi 50 metreden büyükse:
   - Döngüyü sonlandır.
   - Tahliye saatini ekrana yazdır.
   - Kritik su seviyesini ekrana yazdır.
5. Eğer su seviyesi 50 metre veya daha düşükse:
   - Baraj kapaklarını kapalı tut.
   - Saat değişkenini 1 artır.
   - Yeni saatin su seviyesi verisini oku.
6. Su seviyesi kritik eşiği aşana kadar işlemleri tekrarla.
      ## Proje Görselleştirmeleri

### KRİTİK EŞİK Akış Şeması
Aşağıdaki akış şeması, barajdaki su seviyesinin kontrol edilmesini, 50 metre kritik eşiğinin aşılması durumunda döngünün sonlandırılmasını göstermektedir.

![KRİTİK EŞİK Akış Şeması](kritik_esik_akis_semasi.png)

### Örnek Çalışma Çıktısı

Verilen saatlik sensör verileriyle yapılan simülasyonda su seviyesinin 3. saatte 55 metreye ulaşması sonucunda döngü sonlandırılmıştır.

![KRİTİK EŞİK Örnek Çalışma Çıktısı](kritik_esik_ornek_cikti.png)

   ## Kaynakça

- Millî Eğitim Bakanlığı. (Ders kitabının yayın yılı). Bilgisayar Bilimi / Programlama ders kitabı. Millî Eğitim Bakanlığı Yayınları.

**Etik İlke:** Bu proje hazırlanırken yararlanılan kaynaklara saygı gösterilmiş, doğruluk ve dürüstlük ilkeleri benimsenmiştir. Ahilik kültüründeki ustaya saygı ve emeğe değer verme anlayışı, yazılım geliştirme sürecinde kaynak gösterme ve fikrî emeğe saygı ilkeleriyle ilişkilendirilmiştir.
