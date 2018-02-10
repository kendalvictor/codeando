import arcpy

arcpy.env.overwriteOutput=True
arcpy.env.workspace = r"D:\Geotaller\GDB\Practica.gdb"

listaEntidades=arcpy.ListFeatureClasses()

for lista in listaEntidades:
    lista2=arcpy.Describe(lista)
    print lista2.name + "\t" + lista2.Shapetype

print "Script completado"