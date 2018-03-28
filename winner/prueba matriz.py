#!/usr/bin/env python
# -*- coding: cp1252 -*-
#victor villacorta

def Mzeros(M,n): #Analizo si toda una fila o columna son ceros 
    for i in range(n):
        sum_fila,sum_col=0,0
        for j in range(n):
            if M[i][j]>=0:
                sum_col+=M[i][j]
            else:
                sum_col+=M[i][j]*(-1)
            #####################
            if M[j][i]>=0:
                sum_fila+=M[j][i]
            else:
                sum_fila+=M[j][i]*(-1)
        #print sum_col,sum_fila
        if sum_col==0:
            print "\nFila {0} es de solo ceros".format(i+1)
            return True

        if sum_fila==0:
            print "\nColumna {0} es de solo ceros".format(j+1)
            return True
    return False

def MfocLD(M,n): #Analizo si toda una fila o columna son linealmente dependientes
    k=0;
    for i in range(n-1):
        for j in range(i+1,n):
            a=[ ]
            b=[ ]
            k1,k2,n1,n2,li1,li2=-1,-1,n,n,0,0
            for k in range(n):
                #Analisis para filas
                if M[j][k]!=0 and M[i][k]!=0: #Si ambos no son ceros recien almaceno
                    a.append(M[i][k]/M[j][k]) #las divisiones 
                    k1+=1
                elif (M[j][k]==0 and M[i][k]!=0) or (M[j][k]!=0 and M[i][k]==0): 
                    li1=1            #si uno es cero y el otro no, entonces ya son LI
                else:
                    n1=n1-1
                
                ###########
                if k1==0:
                     sum1=a[0]
                elif k1>=1 and a[k1]==a[k1-1]:
                    sum1+=a[k1]

                #Analisis para Columnas
                if M[k][j]!=0 and M[k][i]!=0: #Si ambos no son ceros recien almaceno
                    b.append(M[k][i]/M[k][j]) #las divisiones 
                    k2+=1
                elif (M[k][j]==0 and M[k][i]!=0) or (M[k][j]!=0 and M[k][i]==0): 
                    li2=1            #si uno es cero y el otro no, entonces ya son LI
                else:
                    n2=n2-1
                
                ###########
                if k2==0:
                     sum2=b[0]
                elif k2>=1 and b[k2]==b[k2-1]:
                    sum2+=b[k2]
            if sum1==a[0]*n1 and sum1>0 and li1==0:
                print "Filas {0} y {1} Linealmente Dependientes".format(i+1,j+1)
                return True
            if sum2==b[0]*n2 and sum2>0 and li2==0:
                print 2
                print "Columnas {0} y {1} Linealmente Dependientes".format(i+1,j+1)
                return True
    
    return False

def Mvisualizacion(M,N,n): #Para que la matriz salga en pantalla
    cont=0
    k=0;
    for i in M:
        for j in N:
            if (cont+n-k)%n==0:
                print str(i)+" | "+str(j)
            cont+=1
        k+=1

    
def Midentidad(n): #Creo una matriz identidad de orden n
    N=[ ]
    for i in range(n):
        fila=[ ]
        for j in range(n):
            if i==j:
                a=1
                fila.append(a)
            else:
                a=0;
                fila.append(a)
        print fila
        N.append(fila)
    return N

def DiagonalSinNulos(M,n):
    for i in range(n):
        if M[i][i]==0:
            return i
    return n
            
def op_elemental(M,N,n,i,j,multiplo):
    for k in range(n):
        M[j][k]=M[j][k]-M[i][k]*multiplo
        N[j][k]=N[j][k]-N[i][k]*multiplo

def permuta_fila(M,N,n,i,j):
    for k in range(n):
        val1=M[j][k]
        val2=N[j][k]
        M[j][k]=M[i][k]
        N[j][k]=N[i][k]
        M[i][k]=val
        N[i][k]=val

def div_fila(M,N,n,i,denominador):
    for k in range(n):
        M[i][k]=M[i][k]/denominador
        N[i][k]=N[i][k]/denominador

def detect_fila_posterior(M,n,i):
    for j in range(n):
        if j>i and M[j][i]!=0:
            return j
    return n

                        
def GaussJordan(M,N,n): #El metodo de Gauss Jordan
    for i in range(n):
        if M[i][i]==0:
            j=detect_fila_posterior(M,n,i)
            permuta_fila(M,N,n,i,j)
        if M[i][i]!=1:
            div_fila(M,N,n,i,M[i][i])
        if M[i][i]==1:
            for j in range (i+1,n):
                if(M[i][i]!=0):
                    op_elemental(M,N,n,i,j,M[j][i])
        Mvisualizacion(M,N,n)
        print"**************************"
    for i in range(n):
        if M[n-1-i][n-1-i]==1:
            for j in range(i+1,n):
                op_elemental(M,N,n,n-1-i,n-1-j,M[n-1-j][n-1-i])
                Mvisualizacion(M,N,n)
                print"**************************"

      

print "              INVERSA DE UNA MATRIZ  "
print "                Victor Villacorta  "

matriz=open("matriz.txt","r")
M1=[ ]
col=[ ]
visor,element,n,m=0,0,0,0
#leo la matriz del texto y la muestro
for i in matriz.readlines():
    print i
    fila=i.split(" ")#todos separado por un espacio es un elemento
    M1.append(fila)  #toda la fila es 1er elemento de M
    n+=1             #contara el numero de filas
    m=len(fila)      #numero de columnas de esa fila
    col.append(m)    #guarda el num de columnas de cada fila

#################################verifico num columnas = num filas  1ER FILTRO
for j in col:
    if j!=n:
        visor=1
if visor==1:
    print "\n\nError...no se trata de una matriz cuadrada"
elif visor==0: #####verifico los elementos de la matriz sean numeros 2DO FILTRO
    print "\nMatriz cuadrada detectada"
    M3=[ ]
    for i in range(n):
        M2=[ ]
        for j in range(n):
            try:
                M2.append( float( M1[i][j] ) )
            except: 
                visor=1;
                print "Error.. elemento no numeral detectado y"
                print "        ubicado en la fila {0} columna {1} \n\n".format(i+1,j+1)
                break
        M3.append(M2)

print M3 # donde aca ya tengo todos mis elementos como numeros reales
#Ahora comenzare con el calculo del determinante
det=-1
if visor==0:
    if Mzeros(M3,n)==True: ###Veo si alguna fila o columna sean zeros 3ER FILTRO
        det,visor=0,1
        print "\nDeterminante = {0} \n".format(det)

if visor==0:
    if MfocLD(M3,n)==True: ########Veo si sus filas o columnas son LD 4TO FILTRO
        det,visor=0,1
        print "\nDeterminante = {0} \n".format(det)
    else:
        print "\nFilas o columnas LINEALMENTE INDEPENDIENTES"

if visor ==0:
    #Creo mi matriz identidad
    print "\nCreando matriz identidad: \n"    
    N=Midentidad(n)
    
    #Comienzo con el metodo de gauss-jordan
    print "\nAplicando Metodo de Gauus Jordan: \n"
    #mustro las matrices pegadas una a la otra
    Mvisualizacion(M3,N,n)
    print"**************************"
    GaussJordan(M3,N,n)

print "\n\nMi matriz inversa es : \n"

for i in N:
    print str(i)

print " "


        
    
    






    
    
    
    
    
    
    
    
    
