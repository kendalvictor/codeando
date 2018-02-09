def quicksort(numeros):
    if not numeros:
        return numeros
    primer_elemento = numeros[0]
    menores = [n for n in numeros if n < primer_elemento]
    mayores = filter(lambda n: n > primer_elemento, numeros)
    return quicksort(menores) + \
           [primer_elemento] + \
           quicksort(list(mayores))

print(quicksort([7, 4, 6, 2, 5, 9, 1]))
