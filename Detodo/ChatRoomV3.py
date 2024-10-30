entrada = input()
salvar = ['h', 'e', 'l', 'l', 'o', '']; cont = 0
for i in entrada:
    if i == salvar[cont]:
        cont += 1
print('YES' if cont == 5 else 'NO')
    
