import os
print(os.getcwd())#dosyamızın yolunu verir.
print(os.listdir())#klasörün içindekileri list tipinde verir.
for i in os.listdir():
    print(i)