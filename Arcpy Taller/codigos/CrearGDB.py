import arcpy

#Sobre escribir el resultado
arcpy.env.overwriteOutput=True

#Declarar una variable de entorno
arcpy.env.workspace=r"D:\Publicidad cursos\Taller ArcPy\SHP"

entrada="SuperMercado.shp"
salida="SuperMercado10km.shp"
distancia="10 kilometers"

arcpy.Buffer_analysis(entrada,salida,distancia)

print "Se ha creado el shp a 10 km"