print "matriz vacia :"
matriz=[]
print matriz

print "generando lista vacia con *"
m2 = [0]*5
print m2

print "creando lista de lista tipo matriz"
for i in xrange(5):
    matriz.append([0]*5)
print matriz

print "efecto visual a mi lista de lista tipo matriz"
for i in matriz:
    print "        ",
    for j in i:
        print " ",
        print j,
    print ''

print"Armando un 2x2"
matriz2 = []
for i in xrange(2):
    matriz2.append([0]*2)

def matriz2x2(matriz2):
    for fila in xrange(2):
        for col in xrange(2):
            entero = 0
            while entero == 0:
                try:
                    matriz2[fila][col] = input('('+str(fila)+','+str(col)+') : ')
                    entero = 1
                except:
                    print "Elemento no nunmeral, intente denuevo :"
                    entero = 0
    return matriz2

print matriz2x2(matriz2)








