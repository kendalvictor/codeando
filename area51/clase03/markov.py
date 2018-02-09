import random

archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

contenido = contenido.lower().replace('  ', '').replace('  ', ' ').split(' ')

palabras = {
    'el': ['ingenioso', 'caballero', 'perro']
}

for posicion, palabra in enumerate(contenido[:-1]):
    if palabra not in palabras:
        palabras[palabra] = []
    palabras[palabra].append(contenido[posicion + 1])

oracion = ['el']

for _ in range(10):
    nueva_palabra = random.choice(palabras[oracion[-1]])
    oracion.append(nueva_palabra)

print(' '.join(oracion))
