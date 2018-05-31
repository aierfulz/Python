
import interpolationcsv as interpolation
import writeshape as writes
import raster
import xmls as xml

#define field name and value
field_name = {"name_1": "elev", "name_2": "prec"}

# param = filename
wkt, field = writes.writeShape().readcsv("stations.csv")
writes.writeShape().rewriteshape("point.shp",field_name,field,wkt,1,4326)

#figure
ZI, XI, YI = interpolation.interpolationcsv('stations.csv').draw()

""" 
CONVERT ARRAY,  write tiff this array has been transformed
"""
ZT = ZI[::-1]

transform_Pra_v = raster.raster("dems.tif").writeRaster(4326, XI, YI, ZT)

xml.xmls().writeXML("metadata.xml",transform_Pra_v)