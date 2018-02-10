import arcpy
arcpy.env.overwriteOutput=True
#Declarar Parametros de entrada y salida
inFC = r"C:\compartir\Curso Python\Shapefiles\Departamentos.shp"
extentPol = r"C:\compartir\Curso Python\Shapefiles\Departamentos"
shp=".shp"

#Utilizando la funcion Describe
desc = arcpy.Describe(inFC)
spatialRef = desc.spatialReference

#Matriz que va a contener los puntos
array = arcpy.Array()
i=1
ptList = []
rows = arcpy.SearchCursor(inFC)

for row in rows:
   extent = row.Shape.extent
   array.add(extent.lowerLeft)
   array.add(extent.lowerRight)
   array.add(extent.upperRight)
   array.add(extent.upperLeft)
   array.add(extent.lowerLeft)
   polygon = arcpy.Polygon(array)
   ptList.append(polygon)
   array.removeAll()
   
del rows
del polygon

for dpto in ptList:
	extentPoly=extentPol+str(i).zfill(2)+shp
	arcpy.CopyFeatures_management(dpto,extentPoly )
	arcpy.DefineProjection_management(extentPoly,spatialRef)
	i+=1
#Impresion en pantalla
print "Poligonos creados"