import arcpy
import os

arcpy.env.overwriteOutput=True
EspacioTrabajo = r"D:\Geotaller\GDB"
arcpy.env.workspace = os.path.join(EspacioTrabajo, "Practica.gdb")

xlsFile = open(os.path.join(EspacioTrabajo,"Registros.xls"), "w")
xlsFile.write('Lista de Estaciones' + "\n")
xlsFile.write("===================" + "\n")

registros=arcpy.SearchCursor("Estaciones")

for registro in registros:
    valor=registro.getValue('NOM_ESTAC')
    xlsFile.write("\n" + valor)

xlsFile.close()
print "Script completado" 