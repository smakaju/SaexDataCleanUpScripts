# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 6_SpatialJoin_Paecel&Parcel1.py
# Created on: 2020-10-08 16:18:43.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
CleanPoly = "CleanPoly"
cent = "cent"
NewData111_shp = "C:\\DataCleanTemp\\NewData111.shp"

# Process: Spatial Join
arcpy.SpatialJoin_analysis(CleanPoly, cent, NewData111_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "AREA \"AREA\" true true false 19 Double 0 0 ,First,#,CleanPoly,AREA,-1,-1;PERIMETER \"PERIMETER\" true true false 19 Double 0 0 ,First,#,CleanPoly,PERIMETER,-1,-1;COV1_ \"COV1_\" true true false 10 Long 0 10 ,First,#,CleanPoly,COV1_,-1,-1;COV1_ID \"COV1_ID\" true true false 10 Long 0 10 ,First,#,CleanPoly,COV1_ID,-1,-1;PARCELKEY \"PARCELKEY\" true true false 23 Text 0 0 ,First,#,cent,PARCELKEY,-1,-1;PARCELNO \"PARCELNO\" true true false 10 Long 0 10 ,First,#,cent,PARCELNO,-1,-1;DISTRICT \"DISTRICT\" true true false 10 Long 0 10 ,First,#,cent,DISTRICT,-1,-1;VDC \"VDC\" true true false 10 Long 0 10 ,First,#,cent,VDC,-1,-1;WARDNO \"WARDNO\" true true false 3 Text 0 0 ,First,#,cent,WARDNO,-1,-1;GRIDS1 \"GRIDS1\" true true false 9 Text 0 0 ,First,#,cent,GRIDS1,-1,-1;PARCELTY \"PARCELTY\" true true false 10 Long 0 10 ,First,#,cent,PARCELTY,-1,-1;Shape_Leng \"Shape_Leng\" true true false 19 Double 0 0 ,First,#,cent,Shape_Leng,-1,-1;Shape_Area \"Shape_Area\" true true false 19 Double 0 0 ,First,#,cent,Shape_Area,-1,-1;ParcelNote \"ParcelNote\" true true false 200 Text 0 0 ,First,#,cent,ParcelNote,-1,-1;remarks \"remarks\" true true false 10 Text 0 0 ,First,#,cent,remarks,-1,-1;ORIG_FID \"ORIG_FID\" true true false 10 Long 0 10 ,First,#,cent,ORIG_FID,-1,-1", "CONTAINS", "", "")
