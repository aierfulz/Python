from osgeo import ogr
import os

class readshape:

    def __init__(self,parent = None):

        return

    def readData(self,filename):

        path = os.getcwd() + "\\" + filename
        ds = ogr.Open(path,False)

        layer = ds.GetLayer()

        layerDefine = layer.GetLayerDefn()
        spatial_ref = layer.GetSpatialRef()

        geomType = layerDefine.GetGeomType()

        field_name = []
        for i in range(layerDefine.GetFieldCount()):
            field = layerDefine.GetFieldDefn(i)
            field_content = {"name": field.GetName(),
                             "type": field.GetType(),
                             "width": field.GetWidth(),
                             "precision": field.GetPrecision()
                             }
            field_name.append(field_content)

        geoList, field_value = [], []

        feature = layer.GetNextFeature()

        while feature is not None:
            dic = {}
            geom = feature.GetGeometryRef()
            # print geom , geom.ExportToWkt()
            geoList.append(geom.ExportToWkt())

            for fd in field_name:
                dic[fd["name"]] = feature.GetField(fd["name"])
            field_value.append(dic)

            feature = layer.GetNextFeature()

        return spatial_ref, geomType, field_name, geoList, field_value

