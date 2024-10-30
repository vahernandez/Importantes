entrada = input()
entradaS = entrada.split(" ")
final = []
for i in entradaS:
    final.append(int(i))

rect = int(final[0] * final[1])

if final[0] == final[1] and final[2] == final[0]:
    numero = 1


elif final[0] == final[1] and final[0] > final[2]:
    if final[0] % final[2] != 0:
        numero = int((int(final[0]/final[2]) +1)**2)
    else:
        numero = int((final[0]/final[2])**2)
        
elif final[0] == final[1]  and final[1] < final[2]:
    numero = 1
    
elif final[0] > final [1]  and final[1] > final[2]:
    if final[1] % final[2] != 0 and final[0] % final[2] != 0:
        numero = int((int(final[1]/final[2])+1) * (int(final[0]/final[2])+1))
    elif final[1] % final[2] != 0 and final[0] % final[2] == 0:
        numero = int((int(final[1]/final[2])+1) * (int(final[0]/final[2])))
    elif final[1] % final[2] == 0 and final[0] % final[2] != 0:
        numero = int((int(final[1]/final[2])) * (int(final[0]/final[2])+1))
    elif final[1] % final[2] == 0 and final[0] % final[2] == 0:
        numero = int((int(final[1]/final[2])) * (int(final[0]/final[2])))
elif final[0] > final[1]  and final[1] <= final[2]:
    if final[0] % final[2] != 0 :
        numero = int((int(final[0]/final[2])+1) )
    else:
        numero = int(int(final[0]/final[2]) )



elif final[1] > final [0]  and final[0] > final[2]:
    if final[0] % final[2] != 0 and final[1] % final[2] != 0:
        numero = int(((int(final[1]/final[2]))+1) * ((int(final[0]/final[2]))+1))
    elif final[1] % final[2] != 0 and final[0] % final[2] == 0:
        numero = int((int(final[1]/final[2])+1) * (int(final[0]/final[2])))
    elif final[1] % final[2] == 0 and final[0] % final[2] != 0:
        numero = int((int(final[1]/final[2])) * (int(final[0]/final[2])+1))
    elif final[1] % final[2] == 0 and final[0] % final[2] == 0:
        numero = int((int(final[1]/final[2])) * (int(final[0]/final[2])))
elif final[1] > final[0]  and final[0] <= final[2]:
    if final[1] % final[2] != 0 :
        numero = int((int(final[1]/final[2])+1) )
    else:
        numero = int(int(final[1]/final[2]) )



print(numero)