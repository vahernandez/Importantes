"""
Amugae tiene una oración que consiste en n palabras. Quiere comprimir esta oración en una sola palabra. A Amugae no le gustan las repeticiones, así que cuando fusiona dos palabras 
en una, elimina el prefijo más largo de la segunda palabra que coincide con un sufijo de la primera palabra. Por ejemplo, fusiona "muestra" y "por favor" en "muestrapor favor".

Amugae fusionará su oración de izquierda a derecha (es decir, primero fusionará las dos primeras palabras, luego fusionará el resultado con la tercera palabra, y así sucesivamente). 
Escribe un programa que imprima la palabra comprimida después de que termine el proceso de fusión.

Entrada
La primera línea contiene un entero n (1≤n≤105), el número de palabras en la oración de Amugae.

La segunda línea contiene n palabras separadas por un solo espacio. Cada palabra no está vacía y consiste en letras mayúsculas y minúsculas del alfabeto inglés y dígitos 
('A', 'B', ..., 'Z', 'a', 'b', ..., 'z', '0', '1', ..., '9'). La longitud total de las palabras no excede 106.

Salida
En la única línea, imprime la palabra comprimida después de que termine el proceso de fusión como se describe en el problema.
"""
def merge_words(word1, word2):
    for i in range(min(len(word1), len(word2)), 0, -1):
        if word1[-i:] == word2[:i]:
            return word1 + word2[i:]
    return word1 + word2

def compress_sentence(n, words):
    compressed_word = words[0]
    for i in range(1, n):
        compressed_word = merge_words(compressed_word, words[i])
    return compressed_word

# Lectura de la entrada
n = int(input())
words = input().split()

# Llamada a la función y salida del resultado
print(compress_sentence(n, words))
