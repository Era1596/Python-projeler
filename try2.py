while True:
    try:
        deger=int(input("1. sayıyı giriniz"))
        deger2=int(input("2. sayıyı giriniz"))
        print(deger/deger2)
    except ValueError:
        print("Tam Sayı girmelisin, Program yeniden başlatıldı")

    except ZeroDivisionError:
        print("Bir sayı 0'a bölünemez, Program yeniden başlatıldı")
        continue

