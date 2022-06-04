from cryptography.fernet import Fernet

def dosyaAc(dosya):
    with open(dosya,"rb") as dosya:
        return dosya.read()


def sifrecoz(key,dosya):
    f= Fernet(key)
    icerik = dosyaAc(dosya)
    sifreli=f.decrypt(icerik)
    with open(dosya,"wb") as sifrele:
        sifrele.write(sifreli)




key=dosyaAc("C:\\Users\ogr 6\\PycharmProjects\\ErtugrulRecepAkdag2\\key.txt")
print("C:\\Users\ogr 6\\PycharmProjects\\ErtugrulRecepAkdag2\\key.txt")
dosya = input("Sifresi cözulecek Dosyanin Adi:")

sifrecoz(dosya,key)
