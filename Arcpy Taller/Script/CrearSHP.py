import arcpy

# variables locales
ruta = r"D:\Publicidad cursos\Taller GDB\Python Dia 2\SHP"
nombreNuevoSHP = "MANZANASMIRAFLORES.shp"
tipoGeometria = "POLYGON"
plantilla = ruta+"//"+"Zonas_Vecinales.shp"
medicion = "DISABLED"
elevacion = "DISABLED"
# Use Describe to get a SpatialReference object
referenciaEspacial = arcpy.Describe(template).spatialReference
# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(ruta, nombreNuevoSHP, tipoGeometria, plantilla, medicion, elevacion, referenciaEspacial)

print "SHP CREADO"