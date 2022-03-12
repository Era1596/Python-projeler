while True:
    try:
        def hesapla (a):
            print(a*(a-1))
        a=int(input("Bir Saysı Gir:"))
        hesapla(a)
    except ValueError:
        print("Hatalı Giriş Program Yeniden Başlatılıyor.")
        continue