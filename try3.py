#liste=("345","ali","123a","15","ahmet") bu listeki stringlerden sadece rakam bulunanları ekrana try except kullanarak yaz
try:
    list=int["345,"ali","123a","15","ahmet"]
except ValueError:
    print("hata")
