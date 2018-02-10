import arcpy

arcpy.env.overwriteOutput=True
#Declarar Parametros de entrada y salida
inFC = r"C:\compartir\Curso Python\Shapefiles\Departamentos.shp"
extentPoly = r"C:\compartir\Curso Python\Shapefiles\Departamentosextent.shp"

#Utilizando la funcion Describe
desc = arcpy.Describe(inFC)
extent = desc.extent
spatialRef = desc.spatialReference

#Matriz que va a contener los puntos
array = arcpy.Array()

#Creando el cuadro delimitado por los puntos
array.add(extent.lowerLeft)
array.add(extent.lowerRight)
array.add(extent.upperRight)
array.add(extent.upperLeft)
#Cerrando el poligono
array.add(extent.lowerLeft)

#Creando el objeto poligono
polygon = arcpy.Polygon(array)
array.removeAll()

#Guardando
arcpy.CopyFeatures_management(polygon, extentPoly)
arcpy.DefineProjection_management(extentPoly,spatialRef)
del polygon
#Impresion en pantalla
print "Poligono creado"
