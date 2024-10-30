palabra = input()
min = 0
may = 0
new = ''
for i in palabra:
    if i == i.lower():
        min += 1
    else:
        may += 1
if min>= may:
    new = palabra.lower()
else:
    new = palabra.upper()
print(new)