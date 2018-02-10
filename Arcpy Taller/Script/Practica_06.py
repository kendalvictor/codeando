#Corregir los errores en esta secuencia de comandos para que se imprima
#la misma instruccion 4 veces, usando 4 metodos diferentes:
# 1) Codificacion dura  2) Comas  3) Concatenacion  4) Formato de cadenas

contarLucesTrafico=12
distanciaBuffer='5 Km.'
contarIntersecciones=20

print '1. Encontrado 12 luces en 5 Km. de cobertura y 20 intersecciones'

print '2. Encontrado',contarLucesTrafico,'luces en ',distanciaBuffer,'de cobertura y ',contarIntersecciones,'intersecciones'

print '3. Encontrado '+str(contarLucesTrafico)+' luces en '+distanciaBuffer+' de cobertura y '+str(contarIntersecciones)+' intersecciones'

print '4. Encontrado {0} luces en {1} de cobertura y {2} intersecciones'.format(contarLucesTrafico,distanciaBuffer,contarIntersecciones)