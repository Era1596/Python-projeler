#(a-b) karesini akare - 2a*b + bkare
while True:
    try:
        def kare(a,b):
            print((a-b)**2)
        a=int(input("1. Sayı Ne Olsun:"))
        b=int(input("2. Sayı Ne Olsun:"))
        kare(a,b)
    except ValueError:
        print("Hatalı Giriş Program Yeniden Başlatılıyor.")
        continue