archivo = open('quijote.txt')
contenido = archivo.read().lower().replace(' ', '')
archivo.close()

# 'a': 1
letras = {}

for letra in contenido:
    if letra in 'abcdefghijklmnopqrstuvwxyzñáéíóú':
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

print(letras)