with open ("C:\\inputs\\leer2.txt", "r") as cache1:
    cache2 = cache1.readlines()

for i in cache2:
    print(i.replace("\n", ""))