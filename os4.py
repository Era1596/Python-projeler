
import os
i=input("hangi dosya türünü aratmak istiyorsunuz?")
for i in os.listdir("C:/Users/ogr 6/Desktop/"):
    if i.endswith(('.docx')):
        print(i)
    elif i.endswith('.py'):
        print(i)
    elif i.endswith('.txt'):
        print(i)
    else:
        print("Böyle bir dosya bulunmamakta")