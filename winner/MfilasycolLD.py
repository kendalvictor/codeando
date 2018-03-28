def Mzeros(M,n): #Analizo si toda una fila o columna son ceros 
    z=0
    for i in range(n):
        sum_fila,sum_col=0,0
        for j in range(n):
            sum_col+=M[i][j]
            sum_fila+=M[j][i]
        #print sum_col,sum_fila
        if sum_col==0 or sum_fila==0:
            z=1
            return True
    return False

def MfocLD(M,n): #Analizo si toda una fila o columna son linealmente dependientes
    k=0;
    for i in range(n-1):
        for j in range(i+1,n):
            a=[ ]
            b=[ ]
            k1,k2,n1,n2,li1,li2,sum1,sum2=-1,-1,n,n,0,0,0,0
            for k in range(n):
                #Analisis para filas
                if M[j][k]!=0 and M[i][k]!=0: #Si ambos no son ceros recien almaceno
                    a.append(M[i][k]/M[j][k]) #las divisiones 
                    k1+=1
                elif (M[j][k]==0 and M[i][k]!=0) or (M[j][k]!=0 and M[i][k]==0): 
                    li1=1            #si uno es cero y el otro no entonces ya son LI
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
                    li2=1            #si uno es cero y el otro no entonces ya son LI
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
                print "Columnas {0} y {1} Linealmente Dependientes".format(i+1,j+1)
                return True
    
    return False

    

M=[[06.0, 4.0, 4.0, 6.0], [4.0, 0.0, 2.0, 5.0], [6.0, 0.0, 1.0, 4.0], [3.0, 2.0, 2.0, 3.0]]
print M
visor=0
det=-1
if visor==0:
    if Mzeros(M,4)==True: #Veo si alguna fila o columna sean zeros 3ER FILTRO
        det=0;
        print "\nFila o columna de solo ceros DETECTADA"
        print "Determinante = {0} ".format(det)

if visor==0:
    if MfocLD(M,4)==True: #Veo si sus filas o columnas son LD 4TO FILTRO
        det=0;
        print "Determinante = {0} ".format(det)
    else:
        print "Filas o columnas LINEALMENTE INDEPENDIENTES"



