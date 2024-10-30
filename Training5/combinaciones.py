# Dado un numero binario mayor a 3 digitos, contar las veces que tiene el patron 1 0 1, este patro debe seguir este orden y puede o no
# ser consecutivos ejemplo: 1 0 1 0 0 1 0

num = ['1', '0', '1', '0', '0', '1', '0']
patron = ["1", "0", "1"]
cont=0
k = 0
l = 0
m = 0
for k1 in num[k:-1]:
    l=k+1
    for l1 in num[l:-1]:
        m=l+1
        for m1 in num[m:-1]:
            if k1=="1" and l1=="0" and m1=="1":
                cont+=1
        m=0
        l+=1        
    l=0
    k+=1
print(cont)
    
    