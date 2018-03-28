#!/usr/bin/env python
# -*- coding: cp1252 -*-

import httplib
import os
#######año
a=raw_input("Año a evaluar : ")
e1=int(a)
e1=e1-2000
if e1>3 and e1<10:
        a2="0"+str(e1)
elif e1>9 and e1<16:
        a2=str(e1)
#######mes
m=raw_input("Orden del mes : ")
e2=int(m)
#######dia
d="01"
e3=int(d)
#########
meses=['ENERO','FEBERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
hasta = "D:\SO2_NASA\NASA_"+a+meses[e2-1]
if not os.path.exists(hasta):
        os.makedirs(hasta)

 
#######conexion y descarga
conn = httplib.HTTPConnection("so2.gsfc.nasa.gov:80")
while e3<32:
        try:
                if e3>0 and e3<10:
                        d2="0"+str(e3)
                elif e3>9 and e3<32:
                        d2=str(e3)
                e3=e3+1
                desde = "/pix/daily/"+m+a2+"/peru_so2lf_5k_"+a+m+d2+".jpg"
                conn.request ("GET", "/" + desde)
                r = conn.getresponse()
                r2=r.reason
                if r2=="OK":
                        img = "\NasaSo2"+a+"_"+m+"_"+d2+".jpg"
                else:
                        img = "\NoHallado"+a+"_"+m+"_"+d2+".jpg"
                fichero = file( hasta + "/" + img, "wb" )
                fichero.write(r.read())
                fichero.close()
                print " "+d2+"/"+m+"/"+a+" "+r2

        except:
                pass
                
print "\n Ubicacion de descarga D:\SO2_NASA\NASA_"+a+meses[e2-1]

raw_input("\nPresiona una tecla para salir del scraper.......")
