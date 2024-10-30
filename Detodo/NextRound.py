# los concursantes que tengan mayor o igual al k-esimo lugar avanzaran al siguiente ronda
# Un total de n participantes toman parte de esta competencia. Calcula cuantos participantes pasan a la sig. ronda
# input: la primer linea contiene 2 enteros n y k (1<= k <= n <= 50)
# La segunda linea contiene n enteros a1,a2, .... an (0<=ai<=10), donde ai es la calificacion ganada por el 
# participante del i-esimo lugar
# Output: regresa el numero de participantes que avanzan a la siguiente ronda

nk = input()
lista = input()
nkS = nk.split(" ")
final = []
final2 = []
for i in nkS:
    final.append(int(i))

listaS = lista.split(" ")
for j in listaS:
    final2.append(int(j))
final[1]

cuenta = 0
ind = 1
val = 0
for k in final2:
    if ind == final[1]:
       val = k
    ind += 1
for l in final2:
    if l >= val and l >0:
        cuenta +=1
print(cuenta)
    






    

