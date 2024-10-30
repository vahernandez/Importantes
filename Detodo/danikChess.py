
games = int(input())
whowins = input()
d = 0
a = 0
for i in whowins:
    if i == 'A':
        a+=1
    else:
        d+= 1
if d>a:
    print("Danik")
elif a>d:
    print("Anton")
else:
    print("Friendship")