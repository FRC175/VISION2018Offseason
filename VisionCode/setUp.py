import numpy

###############################################
###############Process Settings################
###############################################
hsvLower = numpy.array([25, 80, 60])
hsvUpper = numpy.array([110,255,255])

blur = 1

cannyThresMin = 10
cannyThreshMax = 12 #Depends thats what needs to be tested

areaMin= 175 #nums need to be tested 
areaMax= 4000
perMin=100
perMax = 1000
imageNum = 3
imagePath = "sample" + str(imageNum) + ".png"
roboRIOIP = #roborio IP for reconization
whRatioMax = 2.3
whRatioMin = 1.45
perimeterRatio = float(4.0/5.5)
perimeterRatioMax = 1.3
perimeterRatioMin = 1.18
minHeight = 18
maxHeight = 150
minWidth = 28
maxWidth = 250
###############################################
###############CAMERA SETTINGS#################
###############################################

res = (640, 360)

centerX = 320
centerY = 180 
framerate = 15 
exposure = 
brightness = 45
sharp = 50
saturation = 50
roto = 180

exposureSet = 