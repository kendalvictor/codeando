import os
print "Ubicacion actual: %s" % os.getcwd()

print r"En el directorio en donde estas hay %d archivos o carpetas" % len(os.listdir(os.getcwd()))

listado= os.listdir(os.getcwd())
for i in listado:
    if os.path.isdir(i):
        print "--> %s es una carpeta" % i
    elif os.path.isfile(i):
        print "--> %s es un archivo" % i
    else:
        print "--> Descripcion de %s desconocida" % i

        
        
