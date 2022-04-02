import os
sayac=0
sayac2=0
deger=input("Hangi dizinde arayayım:")
for kokklasor,altklasorler,dosyalar in os.walk (deger):
    for dosya in dosyalar:
        sayac2=sayac=sayac+1
print(sayac2)