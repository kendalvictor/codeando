lista=[1,2,3,4,9]
print lista
print len(lista)
lista.append(13)
print lista
print len(lista)
lista.insert(2,93)
print lista
print len(lista)
lista.extend([12,14,16])
print lista
print len(lista)

print "####################"
lista1=[4,3,5,6]
M=[lista,lista1]
print M
print len(M)
M[1][1]=100
print M
P=M
lista2=[3,3,5,5]
N=[M,lista2] #M es un elemento lista aparte y lista2 tambien muy aparte
print N #[[[1, 2, 93, 3, 4, 9, 13, 12, 14, 16], [4, 100, 5, 6]], [3, 3, 5, 5]]
M.append(lista2) #lista2 es un elemento lista mas junto con las otras
print M #[[1, 2, 93, 3, 4, 9, 13, 12, 14, 16], [4, 100, 5, 6], [3, 3, 5, 5]]
print P
P.extend(lista2)#cada elemento de lista2 son elementos nuevos individuales
print P #[[1, 2, 93, 3, 4, 9, 13, 12, 14, 16], [4, 100, 5, 6], [3, 3, 5, 5], 3, 3, 5, 5]
print "####################"
g="1 2 3 4 5.2 3.6"
s=g.split(" ")
print g
print s
nuevo=[ ]

for i in s:
    nuevo.append(float(i)+1)

print nuevo
print"#######################"
l1=[1,4,7,3,5,2,8,6]
l2=[10,13,11,14]
l3=[ ]
l3.extend(l1)
print l1
print l2
print l3
l3[2:2]=l2
print l3
l3[8:11]=l2
print l3
l1[0:2]=l2[0:2]
print l1
print"#######################"
print l1[:]   #[10, 13, 7, 3, 5, 2, 8, 6]
print l1[0:3] #[10, 13, 7]
print l1[2:]  #[7, 3, 5, 2, 8, 6]
print l1[:4]  #[10, 13, 7, 3]
print l1[-1]  
print l1[-2]  #orden inverso -1 es el ultimo
print l1[-1:] #toma el ultimo y como no nada delante solo sale el
print l1[:-2] #vota todos los elementos hasta antes del penultimo
print l1[-4:-1] #no vota el ultimo
# al hacer esto [0:3] o esto [-4:-1]
#siempre tomara el primer elemento
#y hasta un alterior a la segunda posicion












    
