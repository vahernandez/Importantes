"""
Hacer un programa que invierta una palabra
"""

palabra = [str(a) for a in input()]

capi = ""
a= 1
for i in palabra:
    capi= capi + palabra[-a]
    a+=1

print(capi)
    