name = input()
new = []
final = [] 
for i in name:
    new.append(i)
    if i not in final:
        final.append(i)
    

if len(final)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
