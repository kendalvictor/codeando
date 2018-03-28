# -*- coding: utf-8 -*-
import random

def lottery():
    # devuelve 6 Numeros entre 1 y 40
    for i in xrange(10):
        yield i

    # devuelve un 7º número entre 1 y 15
    yield random.randint(1,15)

for random_number in lottery():
    print "And the next number is... %d!" % random_number

print "###################"
print lottery(),type(lottery())
generador = lottery()
print "###################"
print generador.next()
print generador.next()
print generador.next()
print generador.next()
print generador.next()
print generador.next()
print generador.next()
