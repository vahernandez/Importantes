# Automatize the process of changing the words with abbreviations. At that all too long words should b replaceb by the 
# abbreviation and the work that are not too long should not undergo any changes.

palabra = input("escribe un palabra: \n")
newW = []
if len(palabra) >= 10:
    newW.append(palabra[0] + str((len(palabra))-2) + palabra[-1])
    print(newW)
else:
    print(palabra)

