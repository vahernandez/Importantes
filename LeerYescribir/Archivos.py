ruta = 'LeerYescribir\lenguajes.txt'
archivo = open(ruta, 'r')
#print (archivo.read())
#print(archivo.readline())
print(archivo.readlines())

archivo.close()

