print("VERİ MAKİNESİNE HOŞ GELDİNİZ")
while True:
    def bilgilerigöster(ad,soyad,adres,tel):
        print("Adınız:",ad)
        print("Soyadınız:",soyad)
        print("Adresiniz:",adres)
        print("Telefon Numaranız:",tel)
    ad2=input("Adınızı Giriniz:")
    soyad2=input("Soyadınızı Giriniz:")
    adres2=input("Adresinizi Giriniz:")
    tel2=input("Telefon Numaranızı Giriniz:")
    bilgilerigöster(ad2,soyad2,adres2,tel2)
    try:
        a=int(input("Programı Tekrar Çalıştırmak İçin 1'e Programı Durdurmak İçin 2'ye Basınız:"))
        if a==1:
            print("Program Yeniden Başlatılıyor")
            continue
        elif a==2:
            print("Program Durduruldu")
            break
    except ValueError:
        print("Hatalı Giriş Program Yeniden Başlatılıyor")
        continue