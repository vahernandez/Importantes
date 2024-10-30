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


credenciales =[input("ingresa tus credenciales: \n") for _ in range(2)]
token = 0
cont = 0
for llave, valor in usuarios.items():
    if llave == credenciales[0] and valor['password'] == credenciales[1]:
        print("Acceso garantizado")
        token +=1
    if token ==1:
        break
    if cont ==2 and token == 0:
        print("Tu usuario o contraseña o los dos son incorrectos por lo tanto no tienes acceso")
    cont += 1
