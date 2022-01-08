import random
while True:
    deger=random.randint(1,9)
    deger2=int(input("1 ile 10 arasında tuttuğum sayıyı tahmin et:"))
    if deger==deger2:
        deger3=int(input("Doğru, programı yeniden başlatmak için 1 e bitirmek için 2 ye bas"))
        if deger3==1:
            print("Program yeniden başlatıldı")
            continue
        elif deger3==2:
            print("Program bitirildi")
            break
    else:
        print("Cevap",deger)
        deger4=int(input("Yanlış, programı yeniden başlatmak için 1 e bitirmek için 2 ye bas"))
        if deger4==1:
            print("Program yeniden başlatıldı")
            continue
        elif deger4==2:
            print("Program bitirildi")
            break
