cuantos = int(input())
vec = []
for i in range((cuantos)):
    vec.append([int(a) for a in input().split(" ")])
tempX = 0; tempY = 0; tempZ = 0
for h in vec:
    tempX = tempX + h[0]; tempY = tempY + h[1]; tempZ = tempZ + h[2]
print(tempX + tempY + tempZ)
if tempX ==0 and tempY == 0 and tempZ == 0:
    print('YES')
else:
    print('NO')

        
        
