# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 3_Copy_Parcel_form_Blank84.py
# Created on: 2020-10-08 10:40:40.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Parcel__3_ = "D:\\LIS_SYSTEM\\LIS_Spatial_Data_Templates\\BLANK84.mdb\\Parcel"
Parcel__5_ = "C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Parcel"

# Process: Copy Features
arcpy.CopyFeatures_management(Parcel__3_, Parcel__5_, "", "0", "0", "0")

