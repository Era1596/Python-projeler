import pyautogui
import time


x=input("Yazdırmak İstediğiniz Veriyi Giriniz:")
c=int(input("Kaç Kere Yazdırcağınızı Giriniz:"))
z=float(input("Yazma Hızıni Giriniz:"))
y=input("Yazdıktan Sonra Enter Butonuna Basılsın mı (Y/N):")
if y == "Y":
    print("5 Saniye Sonra Yazmaya Başlayacak")
    time.sleep(5)
    for i in range(0,c):
        pyautogui.write(x)
        pyautogui.press("enter")
        time.sleep(z)
    print("Yazma İşlemi Bitirildi")
elif y == "N":
    print("5 Saniye Sonra Yazmaya Başlayacak")
    time.sleep(5)
    for i in range(0,c):
        pyautogui.write(x)
        time.sleep(z)
    print("Yazma İşlemi Bitirildi")
