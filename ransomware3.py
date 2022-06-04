from cryptography.fernet import Fernet

def key():
    key2 = Fernet.generate_key()
    with open("key.txt","wb") as file:
        file.write(key2)
    
def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read()
print(key)

def sifrele(key2,dosya):
    f= Fernet(key)
    icerik = dosyaAc(dosya)
    sifreli=f.encrypted(icerik)
    with open(dosya,"wb") as sifrele:
        sifrele.write(sifrele)
        
