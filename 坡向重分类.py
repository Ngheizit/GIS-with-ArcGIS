import arcpy
arcpy.CheckOutExtension("spatial")

img = arcpy.GetParameterAsText(0)

Flat = arcpy.GetParameterAsText(1)
South = arcpy.GetParameterAsText(2)
SouthEath = arcpy.GetParameterAsText(3)
SouthWest = arcpy.GetParameterAsText(4)
East = arcpy.GetParameterAsText(5)
West = arcpy.GetParameterAsText(6)
NorthEast = arcpy.GetParameterAsText(7)
NorthWest = arcpy.GetParameterAsText(8)
North = arcpy.GetParameterAsText(9)
output = arcpy.GetParameterAsText(10)



classes = '-1 0 {0};'.format(int(Flat))
classes += '0 22.5 {0};'.format(int(North))
classes += '22.5 67.5 {0};'.format(int(NorthEast))
classes += '67.5 112.5 {0};'.format(int(East))
classes += '112.5 157.5 {0};'.format(int(SouthEath))
classes += '157.5 202.5 {0};'.format(int(South))
classes += '202.5 247.5 {0};'.format(int(SouthWest))
classes += '247.5 292.5 {0};'.format(int(West))
classes += '292.5 337.5 {0};'.format(int(NorthWest))
classes += '337.5 360 {0};'.format(int(North))

result = arcpy.sa.Reclassify(img, 'Value', classes)
result.save(output)
