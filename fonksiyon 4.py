#girilen değerin karesini hesplayan fonksiyonu yap
while True:
    try:
        def kare(a):
            print(a*a)
        a=int(input("Sayı Ne Olsun:"))
        kare(a)
    except ValueError:
        print("Hatalı Giriş Program Yeniden Başlatılıyor")



