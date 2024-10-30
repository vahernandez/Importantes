"""
Crea una programa de Login que compruebe el usuario y contraseña en el diccionario a continuación:
"""

usuarios = {  
      "iperurena": {  
          "nombre": "Iñaki",  
		  "apellido": "Perurena",  
		  "password": "123123"  
	  },  
	  "fmuguruza": {  
	       "nombre": "Fermín",  
		  "apellido": "Muguruza",  
		  "password": "654321"  
	  },  
	  "aolaizola": {  
	       "nombre": "Aimar",  
		  "apellido": "Olaizola",  
		  "password": "123456"  
	  }  
    }
credenciales = [ input("ingresa tu usuario y contraseña \n") for a in range(2)]

cont = len([a for a in usuarios])
count = 1
for i in usuarios:
    if i == credenciales[0] and usuarios[i]['password'] == credenciales[1]:
        print("Acceso autorizado")
        break
    if cont == count:
        print("El usuario o contraseña son incorrectos")
    count +=1