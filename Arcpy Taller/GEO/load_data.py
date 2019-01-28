#from qgis.core import *
#from processing.tools.vector import VectorWriter

Input_Table = '/home/villacorta/GEO/coordenadas.csv'
lon_field = 'longitude'
lat_field = 'latitude'
crs = 4326
Output_Layer = '/home/villacorta/GEO/points.shp'

spatRef = QgsCoordinateReferenceSystem(
    crs, 
    QgsCoordinateReferenceSystem.EpsgCrsId
)

inp_tab = QgsVectorLayer(
    Input_Table, 'Input_Table', 'ogr'
)
prov = inp_tab.dataProvider()
fields = inp_tab.fields()
outLayer = QgsVectorFileWriter(
    Output_Layer, None, fields, qgis.WKBPoint, spatRef
)

pt = QgsPoint()
outFeature = QgsFeature()

for feat in inp_tab.getFeatures():
    attrs = feat.attributes()
    pt.setX(float(feat[lon_field]))
    pt.setY(float(feat[lat_field]))
    outFeature.setAttributes(attrs)
    outFeature.setGeometry(QgsGeometry.fromPoint(pt))
    outLayer.addFeature(outFeature)
del outLayer