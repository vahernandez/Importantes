listas = [input() for _ in range(5)]

dicc = {}

for i in range(5):
    dicc[f'lista{i+1}'] = [int(a) for a in listas(i).split()]
    
offset = [2,1,0,1,2]
count = 0
ext = 0
for i in dicc:
    if 1 in dicc[i]:
        for j in dicc[i]:
            if 1 == j:
                print(offset[ext ]+ (2- ext) )
                count += 1
    ext +=1