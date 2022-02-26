while True:
    try:
        def topla (a,b):
            print(a+b)
        a=int(input("1. Sayı Ne Olsun:"))
        b=int(input("2. Sayı Ne Olsun:"))
        topla(a,b)
    except ValueError:
        print("Hatalı Giriş Program Yeniden Başlatılıyor.")
        continue
