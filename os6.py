import os
for i in os.listdir("C:/"):
    if i.endswith(('.jpg')):
        print(i)
    else:
        print("Böyle bir dosya bulunmamakta")
