import arcpy
arcpy.env.workspace=r"C:\Curso Python\Dia 2\SHP"
listaSHP=arcpy.ListFeatureClasses()
for shp in listaSHP:
    print shp
    
rutaCopia=r"C:\Users\Richard Flores\Documents\ArcGIS\Default.gdb"
for shp in listaSHP:
    if shp=="Departamentos.shp":
        arcpy.CopyFeatures_management(shp,rutaCopia+"\\Departa")
        

