#Librerias de Geoproceso y Matematicas
import arcpy,math,glob
#Sobrescribir resultados
arcpy.env.overwriteOutput=True
#Variable de entorno
arcpy.env.workspace=r"C:\compartir\Curso Python\Shapefiles"

#Declaramos variables locales
SuperMercado = "SuperMercado.shp"
Inmuebles = "Inmuebles.shp"
Distancias_SM_I="DistanciasSMI.shp"
CapaSalida="Coberturas.shp"
Distrito="DISTRITO"
Alcance="Alcance"
listadisolver=[Distrito,Alcance]
#Creando la capa cobertura
arcpy.Buffer_analysis(SuperMercado,CapaSalida,Alcance,"FULL","ROUND","LIST",listadisolver)
#Utilizando la funcion Describe
desc = arcpy.Describe(Inmuebles)
spatialRef = desc.spatialReference
#Longitud y latitud de Inmuebles
with arcpy.da.SearchCursor(Inmuebles,["SHAPE@XY"]) as cursorXY:
  for row in cursorXY:
    InmX,InmY=row[0]
#Adicionar longitud y latitud a la capa SuperMercado
arcpy.AddXY_management(SuperMercado)
#Adicionar campos InmX, InmY en la capa SuperMercado
arcpy.AddField_management(SuperMercado,"InmX","DOUBLE")
arcpy.AddField_management(SuperMercado,"InmY","DOUBLE")

#Pasar los puntos del inmueble a la capa SuperMercado
arcpy.CalculateField_management(SuperMercado,"InmX",InmX,"PYTHON_9.3","")
arcpy.CalculateField_management(SuperMercado,"InmY",InmY,"PYTHON_9.3","")

#Crear la capa Distancia Super Mercado - Inmueble
arcpy.XYToLine_management(SuperMercado,Distancias_SM_I,"POINT_X","POINT_Y","InmX","InmY","GEODESIC","#",spatialRef)

#Adicionar campo Distancia a la capa Distancias_SM_I
arcpy.AddField_management(Distancias_SM_I,"Distancia","DOUBLE")
arcpy.CalculateField_management(Distancias_SM_I,"Distancia","!Shape.length@METERS!","PYTHON_9.3","")

#Bloque 1 de campo calculado con la funcion llamar_distancia()
campo1 = "Distancia"
expresion1 = "llamar_distancia(!InmX!,!POINT_X!,!InmY!,!POINT_Y!)"
bloquecodigo1 = """def llamar_distancia(InmX,POINT_X,InmY,POINT_Y):
    distancia = math.sqrt((InmX-POINT_X)**2+(InmY-POINT_Y)**2)
    return distancia"""
arcpy.AddField_management(SuperMercado,campo1,"DOUBLE")
arcpy.CalculateField_management(SuperMercado,campo1, expresion1, "PYTHON_9.3", bloquecodigo1)

#Bloque 2 de campo calculado con la funcion cobertura()
campo2 = "Cobertura"
expresion2 = "cobertura(!distancia!,!Alcance!)"
bloquecodigo2 = """def cobertura(distancia,alcance):
    if distancia > alcance:
        return 'SIN COBERTURA'
    else:
        return 'CON COBERTURA'"""	
arcpy.AddField_management(SuperMercado,campo2, "TEXT","#","#","20")
arcpy.CalculateField_management(SuperMercado, campo2, expresion2, "PYTHON_9.3", bloquecodigo2)

#Borrar campos
arcpy.DeleteField_management(SuperMercado,["POINT_X","POINT_Y","InmX","InmY","Distancia"])
arcpy.DeleteField_management(Distancias_SM_I,["POINT_X","POINT_Y","InmX","InmY"])
print "Proceso terminado"