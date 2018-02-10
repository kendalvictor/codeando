#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
import os

arcpy.env.overwriteOutput=True
EspacioTrabajo = r"C:\compartir\Curso Python\GDB"
arcpy.env.workspace = os.path.join(EspacioTrabajo, "practica.gdb")

xlsFile = open(os.path.join(EspacioTrabajo,"Registros.xls"), "w")
xlsFile.write('Lista de Estaciones' + "\n")
xlsFile.write("===================" + "\n")

registros=arcpy.SearchCursor("CentralesHidroelectricas")

for registro in registros:
    valor=registro.getValue('Nomb_Proy')
    xlsFile.write("\n" + valor.encode('utf8'))

xlsFile.close()
print "Script completado" 