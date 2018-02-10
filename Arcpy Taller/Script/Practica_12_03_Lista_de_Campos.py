import arcpy
import os

arcpy.env.overwriteOutput=True

EspacioTrabajo = r"C:\compartir\Curso Python\GDB"

arcpy.env.workspace = os.path.join(EspacioTrabajo, "Practica.gdb")

listaFeatureClass=arcpy.ListFeatureClasses()

xlsFile = open(os.path.join(EspacioTrabajo,"Fields.xls"), "w")
xlsFile.write('FeatureClass' + '\t' + 'Tipo de Geometria' +
              '\t' + 'Campo' + '\t' + 'Tipo de dato')

for lista in listaFeatureClass:
    listafields=arcpy.ListFields(lista)
    lista2=arcpy.Describe(lista)
    xlsFile.write("\n" + lista2.name + "\t" + lista2.Shapetype)
    for listacampos in listafields:
        xlsFile.write("\n" + "\t" + "\t" + listacampos.name + "\t" + listacampos.type)

xlsFile.close()
print "Script completado" 