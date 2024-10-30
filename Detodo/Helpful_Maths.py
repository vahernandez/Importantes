"""
inp = input()
inpS = inp.split("+")
"""

inpS = [int(a) for a in input().split("+")]
inpS.sort()
lista =""

for i in inpS:
    lista+=str(i)+'+'

print(lista[0:-1])



