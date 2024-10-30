"""
in1 = input()
in2 = input()
cont1 = 0
cont2 = 0
cont = []
compara = []
for i in in1:
    for j in in2:
        if cont1 == cont2:
            compara.append(in1[cont1].lower())
            compara.append(in2[cont2].lower())
            compara.sort()
            if compara[0] == compara[1]:
                cont.append(0)
            elif compara[0] == in2[cont1].lower():
                cont.append(1)
            elif compara[0] == in1[cont1].lower():
                cont.append(-1)
        cont2 +=1
    cont2=0
    cont1 +=1
    compara.clear()
final = 0
for h in cont:
    final = final + h
if final > 0:
    print(1)
elif final < 0:
    print(-1)
elif final == 0:
    print(0)    
"""

compara = []
in1 = input()
compara.append(in1.lower())
in2 = input()
compara.append(in2.lower())
compara.sort()
if  in1.lower() == in2.lower():
    cont = 0
elif compara[0] == in1.lower():
    cont = -1
elif compara[0] == in2.lower():
    cont = 1
print(cont) 
    
