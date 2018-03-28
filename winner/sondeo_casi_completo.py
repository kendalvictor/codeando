#!/usr/bin/env python
# -*- coding: cp1252 -*-

a = open("Sondeo.txt","r")
b = open("TTAA.txt","w")

#EXTRAIGO LOS BLOQUES TTAA GENERALES EN UN TXT 
linea=0
encontrado=0
p=0
for i in a.readlines():
	if i.find("TTAA")>0:
		p=linea
		encontrado=1
		b.write(i)
	if linea==p+1 and encontrado==1:
		b.write(i)
	if linea==p+2 and encontrado==1:
		b.write(i)
		b.write("\n")
		p=0
		encontrado=0
		
	linea+=1
a.close()
b.close()
#raw_input()

#EXTRACCION ESPECIFICA DE DATOS CON EL MISMO ORDEN PARA CADA CASO
b = open("TTAA.txt","r")
c = open("850.txt","w")
d = open("700.txt","w")
e = open("500.txt","w")
f = open("400.txt","w")
g = open("300.txt","w")
h = open("250.txt","w")
#tamaño
#text2=b.readlines()
#tam2=len(text2)
linea=0
encontrado=0
for j in b:
    if j.find("TTAA")>0:
        p=linea
        encontrado=1
    if linea==p+1 and encontrado==1:
        k=j.split(" ")
#        print k
        c.write(str(k[21])+"\n") #2 espacios atras del 850
        d.write(str(k[24])+"\n") #2 espacios atras del 700
        e.write(str(k[27]))      #por estar en borde incluye su salto de linea
    if linea==p+2 and encontrado==1:
        m=j.split(" ")
#        print m
        f.write(str(m[20])+"\n") #2 espacios atras del 400
        g.write(str(m[23])+"\n") #2 espacios atras del 300
        h.write(str(m[26])+"\n") #2 espacios atras del 250
        p=0
        encontrado=0
    linea+=1

b.close()
c.close()
d.close()
e.close()
f.close()
g.close()
h.close()
  

#SEPARO DIRECCION DE VELOCIDAD PARA CADA CASO
##############################################850
temp = open("temporal.txt","w")
c = open("850.txt","r")
for k in c:
        r=k[0:3]
        s=k[3:5]
#       i.replace(i[0:5],str(r)+" "+str(s))
        temp.write(str(r)+"\t"+str(s)+"\n")
c.close()
temp.close()
temp = open("temporal.txt","r")
c = open("850.txt","w")
for l in temp:
        c.write(l)
c.close()
temp.close()        

###############################################700
temp = open("temporal.txt","w")
d = open("700.txt","r")
for k in d:
        r=k[0:3]
        s=k[3:5]
        temp.write(str(r)+"\t"+str(s)+"\n")
d.close()
temp.close()
temp = open("temporal.txt","r")
d = open("700.txt","w")
for l in temp:
        d.write(l)
d.close()
temp.close()         

################################################500
temp = open("temporal.txt","w")
e = open("500.txt","r")
for k in e:
        r=k[0:3]
        s=k[3:5]
        temp.write(str(r)+"\t"+str(s)+"\n")
e.close()
temp.close()
temp = open("temporal.txt","r")
e = open("500.txt","w")
for l in temp:
        e.write(l)
e.close()
temp.close()

##################################################400
temp = open("temporal.txt","w")
f = open("400.txt","r")
for k in f:
        r=k[0:3]
        s=k[3:5]
        temp.write(str(r)+"\t"+str(s)+"\n")
f.close()
temp.close()
temp = open("temporal.txt","r")
f = open("400.txt","w")
for l in temp:
        f.write(l)
f.close()
temp.close()

###################################################300
temp = open("temporal.txt","w")
g = open("300.txt","r")
for k in g:
        r=k[0:3]
        s=k[3:5]
        temp.write(str(r)+"\t"+str(s)+"\n")
g.close()
temp.close()
temp = open("temporal.txt","r")
g = open("300.txt","w")
for l in temp:
        g.write(l)
g.close()
temp.close()

###################################################250
temp = open("temporal.txt","w")
h = open("250.txt","r")
for k in h:
        r=k[0:3]
        s=k[3:5]
        temp.write(str(r)+"\t"+str(s)+"\n")
h.close()
temp.close()
temp = open("temporal.txt","r")
h = open("250.txt","w")
for l in temp:
        h.write(l)
h.close()
temp.close() 
raw_input() 
#[]
