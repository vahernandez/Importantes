listas = [input() for _ in range(5)]

dicc = {}

for i in range(5):
    dicc[f'lista{i+1}'] = [int(a) for a in listas[i].split()]
    
cont = 0
ext = 0

offset = [2,1,0,1,2]

for i in dicc:
    print(i)
    if 1 in dicc[i]:
        print(dicc[i])
        for j in dicc[i]:
            if j == 1:
                print(offset[ext] + abs(2-cont))
            cont +=1
    ext += 1
