import arcpy

arcpy.env.workspace=r"D:\Publicidad cursos\Taller ArcPy\GDB\Dia2.gdb"

arcpy.env.overwriteOutput=True

reddomiciliaria="reddomiciliaria"
areaafectada="areaafectada"
distancia="20 Meters"
predios="predios"
prediosafectados="prediosafectados"

arcpy.Buffer_analysis(reddomiciliaria,areaafectada,distancia,"FULL","FLAT","NONE","#")

arcpy.Clip_analysis(predios,areaafectada,prediosafectados,"#")

#print "fin"
arcpy.AddMessage("Geoproceso calculado")