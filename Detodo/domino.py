area = input()
areaS = area.split(" ")
mxn = []
for i in areaS:
    mxn.append(int(i))
cuenta = []
m = mxn[0]
n = mxn[1]
if m >= n:
    cuenta.append((int(m/2)) * n)
    if m % 2 != 0:
        cuenta.append(int(n/2))
    else:
        pass
elif n > m:
    cuenta.append((int(n/2))*m)
    if n % 2 != 0:
        cuenta.append(int(m/2))
    else:
        pass
total = 0
for k in cuenta:
    total = k + total

print(total)
    


