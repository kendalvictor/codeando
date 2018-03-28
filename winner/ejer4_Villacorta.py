#Victor Villacorta  python 2.7
def impresion_ejer4(clock1,clock2,h,m):
    if h>10 and m>10:
        print'\nHora de inicio: {0}. Duracion: {1}. Hora de fin: {2}:{3}'.format(clock1,clock2,str(h),str(m))
    elif h<10 and m>10:
        print'\nHora de inicio: {0}. Duracion: {1}. Hora de fin: 0{2}:{3}'.format(clock1,clock2,str(h),str(m))
    elif m<10 and h>0:
        print'\nHora de inicio: {0}. Duracion: {1}. Hora de fin: {2}:0{3}'.format(clock1,clock2,str(h),str(m))
    elif m<10 and h<0:
        print'\nHora de inicio: {0}. Duracion: {1}. Hora de fin: 0{2}:0{3}'.format(clock1,clock2,str(h),str(m))

def formato_ingreso():
    error=1
    while error==1:
        clock=raw_input(' ._ ')
        if len(clock)>4 and len(clock)==0 and clock.isspace()==True :#verifico longitud adecuada 
            print 'ERROR:longitud de formato invalida'
            continue    
        try: #si la conversion a entero da error, salgo
            hora_actual=int(clock)
        except:
            print 'ERROR: ingreso invalido'
            continue
        #separacion de horas y minutos:
        if len(clock)<3:
            hora=0
            minut=hora_actual
        else:
            hora=hora_actual/100
            minut=hora_actual%100
        if hora>24 or hora<0 or minut>60 or minut<0:#verifico formato de hora
            print 'ERROR: formato de hora incorrecto'
            continue
        else:
            error=0
    return clock,hora,minut
#MAIN
print '-------TIME CALCULATOR----------\nFormato hora inicial: \n1745 para simbolizar 17:45'
#pidiendo los datos
clock1,h1,m1=formato_ingreso()
print 'Duracion (mismo formato):'
clock2,h2,m2=formato_ingreso()

#Y apartir de aca el calculo del resultado
h3=h2+h1
m3=m2+m1
duracion=h2*60+m2
if m3>60:
    m3-=60
    h3+=1
if h3<24:
    impresion_ejer4(clock1,clock2,h3,m3)
else:
    h4=h3/24
    h3=h3%24
    impresion_ejer4(clock1,clock2,h3,m3)  
    
    
    


