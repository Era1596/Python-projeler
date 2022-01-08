import time
import random
sayi=0
while True:
    while sayi== random.randint(0,1000):
        print ("Sayı bulundu")
        break
    sayi=random.randint(0,1000)
    sleep(1.5)