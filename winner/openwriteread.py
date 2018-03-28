a=open("numeros.txt","w")

for n in range(1,11):
    a.write("%d\n"%n)

print "listo"
a.close()
b=open("numeros.txt","r")

for linea in b.readlines():
    print linea.strip("\n")

b.close

