# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 2b_PointCreate.py
# Created on: 2020-10-08 16:08:22.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy


# Local variables:
Parcel1 = "Parcel1"
Points_shp = "C:\\DataCleanTemp\\Points.shp"

# Process: Feature To Point
arcpy.FeatureToPoint_management(Parcel1, Points_shp, "INSIDE")

