

frutafresca = [' banana', ' mora de Logan ', 'maracuya ']
print [arma for arma in frutafresca]
print [arma.strip() for arma in frutafresca] #evita espacios en blanco

vec = [2, 4, 6]
vec2 = [3, 2, 1]
print [[x,x**2] for x in vec]
print [(x, x**2) for x in vec]
print [{x: x**2} for x in vec]
print [x*y for x in vec for y in vec2]
print [vec[i]*vec2[i] for i in range(len(vec))]
'''
[' banana', ' mora de Logan ', 'maracuya ']
['banana', 'mora de Logan', 'maracuya']
[[2, 4], [4, 16], [6, 36]]
[(2, 4), (4, 16), (6, 36)]
[{2: 4}, {4: 16}, {6: 36}]
[6, 4, 2, 12, 8, 4, 18, 12, 6]
[6, 8, 6]
'''
print '################ pi redondeado a varios decimales'
print [str(round(355/113.0, i)) for i in range(1,6)]
'''
['3.1', '3.14', '3.142', '3.1416', '3.14159']
'''
letras={'1era':'Aa','2da':'Bb','3ra':'Cc'}
print '################ directo en el diccionario'
print [x for x in letras]
print [int(x[0]) for x in letras]
print [letras[x] for x in letras]
print [letras[x][0] for x in letras]
print [letras[x][1] for x in letras]

'''
['3ra', '2da', '1era']
[3, 2, 1]
['Cc', 'Bb', 'Aa']
['C', 'B', 'A']
['c', 'b', 'a']

'''
print '################ con items()'
print [x for x in letras.items()]
print [x[0] for x in letras.items()]
print [x[1] for x in letras.items()]
print [x[0][0] for x in letras.items()]
print [x[1][0] for x in letras.items()]
print [x[1][1] for x in letras.items()]

mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print [x for x in mat]
print mat

print '################ uno por uno'
mat1= [x[0] for x in mat]
mat2= [x[1] for x in mat]
mat3= [x[2] for x in mat]

Transpuesta=[mat1,mat2,mat3]
print Transpuesta
'''
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''
print '################ por comprension anidada'
print [[x[i] for x in mat] for i in range(len(x))]
'''
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''
print '################ por zip'
print zip(*mat)
'''
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''






















