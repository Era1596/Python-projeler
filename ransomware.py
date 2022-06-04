from cryptography.fernet import Fernet

def key():
    key2 = Fernet.generate_key()
    with open("key.txt","wb") as file:
        file.write(key2)
    
def dosya():
    with open(dosya,"rb") as dosyam:
        return dosyam.read()
key3=dosya("key.txt")
print(key)

def icerik():
    with open(dosya2,"rb") as dosyam2:
        return dosyam2.read()
key3=dosya2("metin1.txt")
print(metin1)
        
