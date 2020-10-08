# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 12_Construction_SpatialJoin.py
# Created on: 2020-10-08 10:45:53.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: 12_Construction_SpatialJoin <Construction> <Parcel> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Construction = arcpy.GetParameterAsText(0)
if Construction == '#' or not Construction:
    Construction = "C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Construction" # provide a default value if unspecified

Parcel = arcpy.GetParameterAsText(1)
if Parcel == '#' or not Parcel:
    Parcel = "C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Parcel" # provide a default value if unspecified

# Local variables:
Parcel__2_ = Parcel
Parcel__4_ = Parcel__2_
Cons1_shp = "C:\\DataCleanTemp\\Cons1.shp"
Cons1 = Cons1_shp

# Process: Add Field
arcpy.AddField_management(Parcel, "ids", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Parcel__2_, "ids", "[OBJECTID]", "VB", "")

# Process: Spatial Join
arcpy.SpatialJoin_analysis(Construction, Parcel__4_, Cons1_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "SegNo \"SegNo\" true true false 2 Short 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,SegNo,-1,-1;Boundty \"Boundty\" true true false 2 Short 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,Boundty,-1,-1;ParFID \"ParFID\" true true false 4 Long 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,ParFID,-1,-1;MBoundTy \"MBoundTy\" true true false 2 Short 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,MBoundTy,-1,-1;ABoundTy \"ABoundTy\" true true false 2 Short 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,ABoundTy,-1,-1;Shape_Length \"Shape_Length\" false true true 8 Double 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,Shape_Length,-1,-1;MarginName \"MarginName\" true true false 50 Text 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Segments,MarginName,-1,-1;PARCELKEY \"PARCELKEY\" true true false 23 Text 0 0 ,First,#;PARCELNO \"PARCELNO\" true true false 4 Long 0 0 ,First,#;DISTRICT \"DISTRICT\" true true false 2 Short 0 0 ,First,#;VDC \"VDC\" true true false 2 Short 0 0 ,First,#;WARDNO \"WARDNO\" true true false 3 Text 0 0 ,First,#;GRIDS1 \"GRIDS1\" true true false 9 Text 0 0 ,First,#;PARCELTY \"PARCELTY\" true true false 2 Short 0 0 ,First,#;ParcelNote \"ParcelNote\" true false false 200 Text 0 0 ,First,#;Shape_Length_1 \"Shape_Length\" false true true 8 Double 0 0 ,First,#;Shape_Area \"Shape_Area\" false true true 8 Double 0 0 ,First,#;ids \"ids\" true true false 0 Long 0 0 ,First,#,C:\\Users\\DELL\\Desktop\\Coverage_Create\\102-1139-22.mdb\\Parcel,ids,-1,-1", "INTERSECT", "", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(Cons1_shp, "ParFID", "[ids]", "VB", "")

