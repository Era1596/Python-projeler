#klavyeden e harfi girildiğinde ekrana erkek, k harfi girildiğinde kız yazılacak
deger=input("E veya K giriniz:").lower()
if deger=="e":
    print("Erkek")
elif deger=="k":
    print("Kız")
else:
    print("Böyle bir değer yok")
