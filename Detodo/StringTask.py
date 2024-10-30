



palabra = [str(a) for a in input().lower()]
sinv = ''
voc = ['a', 'e', 'i', 'o', 'u', 'y']
for i in palabra:
    if i not in voc:
        sinv += '.'+i
print(sinv)
        
 
