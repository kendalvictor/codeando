import arcpy
import os

arcpy.env.overwriteOutput=True

EspacioTrabajo = r"C:\compartir\Curso Python\GDB"

arcpy.env.workspace = os.path.join(EspacioTrabajo, "mundo.gdb")

listadataset=arcpy.ListDatasets()

xlsFile = open(os.path.join(EspacioTrabajo,"Dataset.xls"), "w")
xlsFile.write('Lista de Datasets' + "\n")
xlsFile.write('=================' + "\n")

for lista in listaFeatureClass:
    lista2=arcpy.Describe(lista)
    xlsFile.write("\n" + lista2.name + "\t" + lista2.Shapetype)

xlsFile.close()
print "Script completado" 