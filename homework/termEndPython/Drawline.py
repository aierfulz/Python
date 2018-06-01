
#--------------------------------

class readlineArray:

    def readfile(self,path):
        file = open(path, "r")
        content = file.readlines()
        temp = []
        carID = []
        cols = ""
        k = len(content)
        for i in range(len(content)):
            result = content[i].split(',')
            carID.append(result[0])
        for i in range(len(carID) - 1):
            if (carID[i] == carID[i + 1]):
                col = (content[i].split(','))[3] + ' ' + (content[i].split(','))[4] + ","
                cols = cols + col
            else:

                cols = cols + (content[i].split(','))[3] + ' ' + (content[i].split(','))[4]
                temp.append(carID[i] + '/' + cols)
                cols = ""
        cols = cols + (content[k - 1].split(','))[3] + ' ' + (content[k - 1].split(','))[4]
        temp.append(carID[k - 1] + '/' + cols)
        return temp

    def Drawlines(self, path, lineArray):

        from osgeo import ogr, osr
        filename = path

        driver = ogr.GetDriverByName("ESRI Shapefile")
        ds = driver.CreateDataSource(filename)
        spatialref = osr.SpatialReference('GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]')

        layer = ds.CreateLayer(filename, srs=spatialref, geom_type=ogr.wkbLineString)

        field = ogr.FieldDefn("CarId", ogr.OFTInteger)
        layer.CreateField(field)

        for i in range(len(lineArray)):
            wkt = "LINESTRING" + '(' + lineArray[i].split("/")[1] + ')'
            wkt_line = ogr.CreateGeometryFromWkt(wkt)
            line = ogr.Feature(layer.GetLayerDefn())
            line.SetGeometry(wkt_line)
            line.SetField("CarId", lineArray[i].split("/")[0])
            layer.CreateFeature(line)

        ds.Destroy()

    def readshape(self,path):

        from osgeo import ogr, osr

        ds = ogr.Open(path, False)
        layer = ds.GetLayer(0)
        layerDefine = layer.GetLayerDefn()
        geomtype = layerDefine.GetGeomType()
        sourceref = layer.GetSpatialRef()
        fieldlist = []

        for i in range(layerDefine.GetFieldCount()):
            fieldDefine = layerDefine.GetFieldDefn(i)
            fieldDict = {'name': fieldDefine.GetName(),
                         'type': fieldDefine.GetType(),
                         'width': fieldDefine.GetWidth(),
                         'decimal': fieldDefine.GetPrecision()
                         }
            fieldlist = fieldlist + [fieldDict]

        geomlist, reclist = [], []
        feature = layer.GetNextFeature()

        while feature is not None:
            geom = feature.GetGeometryRef()
            geomlist = geomlist + [geom.ExportToWkt()]
            rec = {}
            for fd in fieldlist:
                rec[fd['name']] = feature.GetField(fd['name'])
            reclist += [rec]
            feature = layer.GetNextFeature()

        return geomtype,sourceref,fieldlist,geomlist,reclist

    def writeshape(self,filename,spatialref,geomtype,fieldlist,geomlist,reclist):

        from osgeo import ogr, osr
        driver = ogr.GetDriverByName("ESRI Shapefile")
        ds = driver.CreateDataSource(filename)

        spatialrefs = osr.SpatialReference()
        spatialrefs.ImportFromEPSG(spatialref)
        spatialrefs.ExportToWkt()

        layer = ds.CreateLayer(filename, srs=spatialrefs, geom_type=geomtype)

        for fd in fieldlist:
            field = ogr.FieldDefn(fd['name'], fd['type'])
            if fd.has_key('width'):
                field.SetWidth(fd['width'])
            if fd.has_key('decimal'):
                field.SetPrecision(fd['decimal'])
            layer.CreateField(field)

        for i in range(len(reclist)):
            geom = ogr.CreateGeometryFromWkt(geomlist[i])
            feat = ogr.Feature(layer.GetLayerDefn())
            feat.SetGeometry(geom)
            for fd in fieldlist:
                feat.SetField(fd['name'], reclist[i][fd['name']])
            layer.CreateFeature(feat)

        ds.Destroy()

    def projectTransform(self,sourceref,targetref,geomlist):

        from osgeo import ogr, osr

        targetrefs = osr.SpatialReference()
        targetrefs.ImportFromEPSG(targetref)
        targetrefs.ExportToWkt()

        coorfTrans = osr.CoordinateTransformation(sourceref, targetrefs)

        for i in range(len(geomlist)):
            geom = ogr.CreateGeometryFromWkt(geomlist[i])
            geom.Transform(coorfTrans)
            geomlist[i] = geom.ExportToWkt()
        return geomlist

# if __name__ == '__main__':
#
#     pathfile = r"C:\Users\giser\Desktop\test.txt"
#     pathline = r"C:\Users\giser\Desktop\20171013\test.shp"
#     pathlineref = r"C:\Users\giser\Desktop\20171013\test_new.shp"
#     targetref = 3785
#
#     temp = readlineArray().readfile(pathfile)
#     readlineArray().Drawlines(pathline,temp)
#
#     geomtype, sourceref, fieldlist, geomlist, reclist = readlineArray().readshape(pathline)
#     geomlist = readlineArray().projectTransform(sourceref,targetref,geomlist)
#     readlineArray().writeshape(pathlineref,targetref,geomtype,fieldlist,geomlist,reclist)
#
#     print "success

