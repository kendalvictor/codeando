import time
from threading import Thread


def myfunc(i):
    for j in range(100000000):
        j += 1


def hilado(func):
    def decorador(*args, **kwargs):
        hilo = Thread(target=func, args=args, kwargs=kwargs, name="HiloPrueba")
        hilo.start()
        hilo.join()
    return decorador


@hilado
def funcion_prueba(n):
    for i in range(n):
        myfunc(i)

comienzo = time.time()
funcion_prueba(5)
print(time.time() - comienzo)


