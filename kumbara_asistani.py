atilan_tl=float(input("Kumbarana kaç tl attın="))
guncel_kur=float(input("Dolar kurunu girin="))
dolar=atilan_tl/guncel_kur
print(f"\nKumbaraya eklenen tutar: {atilan_tl:.2f} TL")
print(f"Güncel döviz kuru: {guncel_kur:.2f}")
print(f"Kumbaradaki artışın döviz karşılığı: {dolar:.2f} Dolar")