while True:
    try:
        print("HESAP MAKİNESİ")
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")
        print("5 - Çıkış")
        x=input("Hangi İşlemi Yapmak İstiyorsun:")
        if x=="1":
            a=int(input("1. Sayı:"))
            b=int(input("2. Sayı:"))
            print(a+b)
        elif x=="2":
            a=int(input("1. Sayı:"))
            b=int(input("2. Sayı:"))
            print(a-b)
        elif x=="3":
            a=int(input("1. Sayı:"))
            b=int(input("2. Sayı:"))
            print(a*b)
        elif x=="4":
            a=int(input("1. Sayı:"))
            b=int(input("2. Sayı:"))
            print(a/b)
        elif x=="5":
            print("Program Sonloandırılıyor...")
            break
        else:
            print("Hatalı Giriş Lütfen Tekrar Deneyiniz")
            continue
    except(ValueError):
        print("Hatalı Giriş Lütfen Tekrar Deneyiniz")
        continue
        