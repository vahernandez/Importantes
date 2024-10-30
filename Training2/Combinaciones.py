# Dado un numero binario mayor a 3 digitos, contar las veces que tiene el patron 1 0 1, este patro debe seguir este orden y puede o no
# ser consecutivos ejemplo: 1 0 1 0 0 1 0

num = ['1', '0', '1', '0', '0', '1', '0']
patron = ["1", "0", "1"]

K='1'
J='0'
I = ''
a=0
b= a + 1
c=b+1

cuenta = 0
for k in num[a:len(num)+1]:
    K = num[a]
    for j in num[(b): len(num)+1]:
        J=num[b]
        for i in num[c : len(num)+1]:
            I=num[c]
            if K=='1' and J == '0' and I =='1':
                cuenta +=1
            c +=1
        c = b+1
        b += 1
    b = a + 1
    a += 1
print(cuenta)