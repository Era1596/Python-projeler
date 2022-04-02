#listdir ile sadece bir klasörün içerisini görebiliyor klasörlerin içerisdindeki klasörleride görebilmek için os.walk fonksiyonu kullanılır
import os
for i in os.walk("C:/Users/ogr 6/Desktop/elma/"):
    print(i)