palabra = input('ingresa una palabra: ')

if palabra == palabra[::-1]:
    print('es palíndromo')
else:
    print('no es palíndromo')
