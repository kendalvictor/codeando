import arcpy

#Sobre escribir el resultado
arcpy.env.overwriteOutput=True

entrada=arcpy.GetParameterAsText(0)
salida=arcpy.GetParameterAsText(1)
distancia=arcpy.GetParameterAsText(2)

arcpy.Buffer_analysis(entrada,salida,distancia)

#print "Se ha creado el shp a 10 km"
arcpy.AddMessage("Buffer creado")