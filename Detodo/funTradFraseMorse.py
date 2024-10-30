"""
Crea una función que tradusca una frase a código morse
"""

equivalencias = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.", 
    "-": "-....-",
}

frase = "SOS"
fraseS= list(frase)
print(fraseS)
traduccion = []
cuenta = 0
"""
for i in fraseS:
    cuentas = 0
    for j in equivalencias:
        if fraseS[cuenta] == list(equivalencias.keys())[cuentas]:
            #print( equivalencias[list(equivalencias.keys())[cuentas]])
            traduccion.append(equivalencias[list(equivalencias.keys())[cuentas]])
            break
        #print(list(equivalencias.keys())[cuentas])
        cuentas = cuentas + 1
    cuenta = cuenta + 1    
print(traduccion)
"""
#print (equivalencias["1"])

for i in fraseS:
    cuentas = 0
    for j in equivalencias:
        if i == j:
            #print( equivalencias[j])
            traduccion.append(equivalencias[j])
            break
        #print(list(equivalencias.keys())[cuentas])
        cuentas = cuentas + 1
    cuenta = cuenta + 1    
print(traduccion)