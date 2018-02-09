def es_primo(numero):
    # raiz_numero = int(numero ** 1/2)
    # lista = range(2, raiz_numero)
    # divisores = map(lambda n: numero % n == 0, lista)
    # return not any(divisores)

    for n in range(2, int(numero ** 1/2)):
        if numero % n == 0:
            return False
    return True

numero_ridiculamente_grande = 600851475143
#
# for n in reversed(range(2, numero_ridiculamente_grande)):
#     print('Probando', n)
#     if numero_ridiculamente_grande % n == 0 and es_primo(n):
#         print('Encontrado:', n)

factores = []

for n in range(2, int(numero_ridiculamente_grande ** 1/2)):
    if numero_ridiculamente_grande % n == 0:
        if es_primo(numero_ridiculamente_grande / n):
            factores.append(numero_ridiculamente_grande / n)
        if es_primo(n):
            factores.append(n)

print(max(factores))
