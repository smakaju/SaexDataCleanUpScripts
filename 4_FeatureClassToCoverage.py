# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 4_FeatureClassToCoverage.py
# Created on: 2020-10-08 10:41:01.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: 4_FeatureClassToCoverage <Parcel1_shp__2_> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy

# Script arguments
Parcel1_shp__2_ = arcpy.GetParameterAsText(0)
if Parcel1_shp__2_ == '#' or not Parcel1_shp__2_:
    Parcel1_shp__2_ = "C:\\DataCleanTemp\\Parcel1.shp" # provide a default value if unspecified

# Local variables:
cov1 = "C:\\DataCleanTemp\\cov1"
Parcel_Rename = "C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Parcel_Rename"
Parcel1_shp = "C:\\DataCleanTemp\\Parcel1.shp"

# Process: Feature Class To Coverage
arcpy.FeatureclassToCoverage_conversion("C:\\DataCleanTemp\\Parcel1.shp REGION", cov1, "0.005 Meters", "DOUBLE")

