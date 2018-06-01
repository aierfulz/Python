import os
from osgeo import ogr, osr
import csv

class writeShape:

    def readcsv(self,filename):
        wkt = []
        filed = []
        files = open(os.getcwd() + "\\" + filename, 'r')

        for line in csv.reader(files):
    #
            try:
                lot, lat, altitude, pre = line[0], line[1], line[2], line[3]
                wkt.append("POINT" + "(" + lot + ' ' + lat + ')')
                filed.append(pre + "," + altitude)

            except Exception as e:
                print e
                pass
        return wkt,filed


    #field_name = {"name_1": "elev", "name_2": "prec"}

    def rewriteshape(self,filename,field_name,field_value,wkt,geom_types,spatial_ref_tag):
        driver = ogr.GetDriverByName("ESRI Shapefile")
        ds = driver.CreateDataSource(filename)

        spatial_ref = osr.SpatialReference()
        spatial_ref.ImportFromEPSG(spatial_ref_tag)
        spatial_ref.ExportToWkt()

        # geom_type == 1 point ==2 Line  ==3 polygon

        layer = ds.CreateLayer(filename, srs=spatial_ref, geom_type=geom_types)

        #
        for name in field_name.keys():
            fileds = ogr.FieldDefn(field_name[name], ogr.OFTReal)
            layer.CreateField(fileds)

        # string not number from start to end
        for i in range(1, len(wkt)):

            geom = ogr.CreateGeometryFromWkt(wkt[i])
            feature = ogr.Feature(layer.GetLayerDefn())
            feature.SetGeometry(geom)
            for k in range(len(field_name.keys())):
                feature.SetField(field_name[field_name.keys()[k]], str(field_value[i]).split(",")[k])
            layer.CreateFeature(feature)

        ds.Destroy()

