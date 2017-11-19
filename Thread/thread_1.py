import time
from threading import Thread


def myfunc(i):
    for j in range(100000000):
        j += 1


print("/////// SIN HILOS:: ", end=" ")
comienzo = time.time()
for i in range(5):
    myfunc(i)
print(time.time() - comienzo)


print("/////// CON HILOS:: ", end=" ")

comienzo = time.time()
for i in range(5):
    t = Thread(target=myfunc, args=(i, ))
    print("i ", i)
    t.start()
    t.join()
print(time.time() - comienzo)

print("fin")



