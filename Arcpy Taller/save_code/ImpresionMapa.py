import arcpy
mxd = arcpy.mapping.MapDocument(r"Mapass.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    print "Exporting page {0} of {1}".format(
        str(mxd.dataDrivenPages.currentPageID), 
        str(mxd.dataDrivenPages.pageCount)
    )
    arcpy.mapping.ExportToPDF(mxd, r"D:\Publicidad cursos\Taller ArcPy\Reportes\ddp\Departamentos_Pag" + str(pageNum) + ".pdf")
del mxd