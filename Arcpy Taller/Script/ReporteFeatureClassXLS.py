import arcpy

arcpy.env.overwriteOutput=True

arcpy.env.workspace = r"D:\Geotaller\GDB\Practica.gdb"

listaFeatureClass=arcpy.ListFeatureClasses()

xlsFile = open(r"D:\Geotaller\Reportes\Estaciones.xls", "w")
xlsFile.write('FeatureClass' + "\t" + 'Tipo de Geometria')

for lista in listaFeatureClass:
    lista2=arcpy.Describe(lista)
    xlsFile.write("\n" + lista2.name + "\t" + lista2.Shapetype)

xlsFile.close()

print "Script completado"