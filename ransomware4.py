from cryptography.fernet import Fernet

def keyUret():
    key=Fernet.generate_key()
    with open("C:\\Users\ogr 6\\PycharmProjects\\ErtugrulRecepAkdag2\\key.txt","wb") as file:
        file.write(key)
    
def dosyaAc(dosya):
    with open(dosya,"rb") as dosya:
        return dosya.read()


def sifrele(key,dosya):
    f= Fernet(key)
    icerik = dosyaAc(dosya)
    sifreli=f.encrypt(icerik)
    with open(dosya,"wb") as sifrele:
        sifrele.write(sifreli)

key=dosyaAc("C:\\Users\ogr 6\\PycharmProjects\\ErtugrulRecepAkdag2\\key.txt")
print("C:\\Users\ogr 6\\PycharmProjects\\ErtugrulRecepAkdag2\\key.txt")
dosya = input("Şifrelenecek Dosyanın Adı:")

keyUret()
dosyaAc(dosya)
sifrele(key,dosya)
