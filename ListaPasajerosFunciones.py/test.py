pasajeros= [("Manuel Juarez", 19823451, "Glasgow"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 910626, "Glasgow")]
paises= [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")]

pais = "Escocia"
cuenta = 0
for i in pasajeros:
    for j in paises:
        print(j[1])
        print(i[2], j[0])
        if pais == j[1] and i[2] == j[0]:
            cuenta = cuenta +1
print (cuenta)
