#girilen sayının 5 katının 3 eksiğinin yarısını hesaplayın
while True:
    try:
        def islem(a):
            print("Sonuç",(a*5-3)/2)
        a=int(input("Sayı Ne Olsun:"))
        islem(a)
    except ValueError:
        print("Hatalı Giriş Program Yeniden Başlatılıyor.")
        continue

