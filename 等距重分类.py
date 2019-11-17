import arcpy
arcpy.CheckOutExtension("spatial")


img = arcpy.GetParameterAsText(0)
classCount = int(arcpy.GetParameterAsText(1))
lenght = int(arcpy.GetParameterAsText(2))
output = arcpy.GetParameterAsText(3)

interval = lenght / classCount

i = 0
value = classCount
classes = ''
while(i < lenght):
    classes += '{0} {1} {2};'.format(i, i + interval, value)
    i += interval
    value -= 1


result = arcpy.sa.Reclassify(img, 'Value', classes)
result.save(output)

