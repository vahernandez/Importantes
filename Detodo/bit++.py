num = int(input())
exp = input()
expS = exp.split(" ")
temp = 0

for i in expS:
    if i == 'x--' or i == '--x' or i == 'X--' or i == '--X' or i == 'X-- ' or i == '--X ':
        temp-=1
    #elif i == 'x++' or i == '++x' or i == 'X++' or i == '++X' or i == 'X++ ' or i == '++X ':
    else:
        temp+=1
print(temp)
