
from osgeo import gdal
from osgeo import osr
import os
import numpy as np
import math
import xml.dom.minidom as xml
class raster:

    def __init__(self,filename):

        self.file_name = filename

        return

    def  writeRaster(self, spatial,X, Y, raster_data):
        transform_Pra = {}

        driver = gdal.GetDriverByName("GTiff")
        path = os.getcwd() + '\\' + self.file_name

        col, row = np.shape(raster_data)
        cell_COL = math.floor((np.max(X) - np.min(X)) / 100)
        cell_ROW = math.floor((np.max(Y) - np.min(Y)) / 100)

        geo_trans = [np.min(X), cell_COL, 0, np.max(Y), 0, -cell_ROW]
        #geo_trans = [np.min(X), cell_ROW, 0, np.min(Y), 0, -cell_COL]

        i = 0
        value = ["topX", "pixelX", "offAngleX", "topY", "offAngleY", "pixelX"]
        for name in geo_trans:
            try:
                transform_Pra[value[i]] = name
            finally:
                pass

            i = i + 1


        spatial_ref = osr.SpatialReference()
        spatial_ref.ImportFromEPSG(spatial)
        spatial_ref.ExportToProj4()

        metadata = spatial_ref.ExportToXML()

        dst_ds = driver.Create(path, col, row, 1, gdal.GDT_Float64)
        #dst_ds = driver.Create(path, row, col, 1, gdal.GDT_Float64)

        dst_ds.SetGeoTransform(geo_trans)
        dst_ds.SetProjection(str(spatial_ref))

        #dst_ds.SetProjection('PROJCS["WGS_1984_UTM_Zone_50N",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",117],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AUTHORITY["EPSG","32650"]]')
        dst_ds.GetRasterBand(1).WriteArray(raster_data)

        return transform_Pra

    def readRaster(self):

        path = os.getcwd() + "\\" + self.file_name
        dataset = gdal.Open(path)

        geo_trans = dataset.GetGeoTransform()

        return geo_trans
