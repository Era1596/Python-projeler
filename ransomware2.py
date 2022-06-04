from cryptography.fernet import Fernet

with open("key.txt","rb") as file:
    with open("key2.txt","wb") as file:
        file.write(key)