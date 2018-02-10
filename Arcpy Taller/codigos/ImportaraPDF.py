import arcpy
mxd=arcpy.mapping.MapDocument("CURRENT")
arcpy.mapping.ExportToPDF(mxd,r"D:\Publicidad cursos\Taller ArcPy\Reportes\formalizacion.pdf")

