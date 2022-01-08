liste=[]
while True:
    for i in range (5):
        deger=input("Sayı giriniz:")
        liste.append(deger)
    deger2=input("Bayılar büyükten küçüğe sıralanacaksa b küçükten büyüğe sıralanacaksa k giriniz:").upper()
    if deger2 == "K":
        liste.sort()
        print(liste)
        print("İşlem tamamlandı tekrar sayı girebilir veya programdan çıkabilirsiniz")
    elif deger2 == "B":
        liste.sort(reverse=True)
        print(liste)
        print("İşlem tamamlandı tekrar sayı girebilir veya programdan çıkabilirsiniz")
    else:
        print("Hatalı giriş tekrar başlatıldı")
        continue
