import threading

def contar(bloque):
    for _ in bloque:
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'read:', _)

NUM_HILOS = 4
list_print = range(100)
n = len(list_print)

for i,num_hilo in enumerate(range(NUM_HILOS)):
    hilo = threading.Thread(
        name='hilo%s' %num_hilo, target=contar,
        args=[list_print[int(i*n/4):int((i+1)*n/4)]]
    )    
    hilo.start()

print("FIN")
