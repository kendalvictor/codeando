import time
import random


def last_fibonaci(ultimo_numero, b=1, a=0):
    """
    :param last_fib: Numero entero mayor a cero
    :param b: Segundo varlor inicial de la serie fibonacci, delfault = 1
    :param a: Primer varlor inicial de la serie fibonacci, delfault = 0
    :return: Dos ultimos valores de la serie de fibonacci menores que el
    numero ingresado mediante recursion
    """
    if b >= ultimo_numero:
        print(a, b - a)
        return

    last_fibonaci(ultimo_numero, b=a + b, a=b)


def get_print_inversa(matriz):
    """
    Imprimire una version de transpuesta de una matriz reflejada en su 2da
    diagonal
    :param matriz (lista de listas, donde el tamaño de cada sublista es
    igual al de la lista que las contiene):
    :return:
    """
    tamanno = matriz.__len__()
    ref = tamanno + 1
    i = 1  #incide horizontal
    j = 1  #indice vertical
    while True:
        (new_i, new_j) = (i, j) if i + j == ref else (ref - j, ref - i)
        print(matriz[new_i - 1][new_j - 1], end='  ')

        if j == tamanno:
            print(" ")
            j = 0
            i += 1

            if i > tamanno:
                del matriz
                break
        j += 1


def order_list(lista_numeros):
    """
    :param lista_numeros: Lista de numeros
    :return: Lista ordenada y sin elementos repetidos mediante recursion
    """
    if not lista_numeros:
        return lista_numeros
    elemento_azar = random.choice(lista_numeros)
    menores = list({n for n in lista_numeros if n < elemento_azar})
    mayores = list({n for n in lista_numeros if n > elemento_azar})
    return order_list(menores) + [elemento_azar] + order_list(mayores)

if __name__ == '__main__':
    print("Ejercicio 1: ")
    inicio_finonacci = time.time()
    last_fibonaci(6765)
    print('tiempo de ejecucion : ', (time.time() - inicio_finonacci) * 1000,
          ' milisegundos \n')
    print("Ejercicio 2: ")
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    inicio_while = time.time()
    get_print_inversa(matriz)
    print('tiempo de ejecucion : ', (time.time() - inicio_while) * 1000,
          ' milisegundos \n')

    print("Ejercicio 3: ")
    lista_evaluacion = [10, 8, 1, 1, 3, 6, 2, 10, 3]
    inicio_orden = time.time()
    print(order_list(lista_evaluacion))
    print('tiempo de ejecucion : ', (time.time() - inicio_orden) * 1000,
          ' milisegundos \n')