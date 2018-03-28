# -*- coding: cp1252 -*-
import socket
import time
import os

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('so2.gsfc.nasa.gov', 80))
a=raw_input("Año a evaluar : ")
m=raw_input("Orden del mes : ")
d=raw_input("dia deseado : ")
misock.send('GET http://so2.gsfc.nasa.gov'+a+m+d+'HTTP/1.0\n\n')
contador = 0
imagen = "";
while True:
    datos = misock.recv(5120)
    if ( len(datos) < 1 ) : break
    # time.sleep(0.25)
    contador = contador + len(datos)
    imagen = imagen + datos
print misock  
misock.close()
pos = imagen.find("\r\n\r\n");
imagen = imagen[pos+4:]
hasta = "D:\SO2_NASA"
if not os.path.exists(hasta):
    os.makedirs(hasta)    
nasa = open(hasta+"\SO2_"+a+m+d+".jpg","wb")
nasa.write(imagen);
nasa.close()

