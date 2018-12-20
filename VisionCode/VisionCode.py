import time 
import logging 
import setUp
import cv2 
import numpy 
import arsparse
from threading import Thread
from networktables import NetworkTable #May run into errors 
from camera.array import CameraRGBArray #camera import 
from camera import Camera #What cammera to use

class VisionCode:
    def __init__(self):
        self.camera = Camera()
        self.camera.brightness = setUp.brightness
        self.camera.sharpness = setUp.sharp
        self.camera.saturation = setUp.saturation
        self.camera.resolution = setUp.res
        self.camera.framerate = setUp.framerate
        self.camera.shutter_speed = setUp.exposure
        self.camera.rotation = setUp.roto
        self.rawCapture =  PiRGBArray(self.camera, size=setUp.resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
        self.image = None
        self.stopped = False 


    def running(self):
        Thread(target=self.update, args=()).start)
        return self 

    def updateData(self):
        for frame in self.stream:
            self.image = frame.array
            self.rawCapture.truncate(0)

            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.clase()
                return self
    def processingTheImage(ori):
        outImage = cv2.cvtColor(ori, cv2.)
        outImage = cv2.inRange(setUp.hsvLower, setUp.hsvUpper)
        outImage = cv2.Gassiunblur(outImage, 3)
        outImage = cv2.Canny(utImage, setUp.cannyThreshMin, setUp.cannyThreshMax)
        ##CONTOUR FINDS
         (outImage, contours, _) = cv2.findContours(outImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
         outImage = cv2.drawContours(origImage, contours, -1, (255, 255, 0), 1)
         contoursFinal = []
         
         for contour in contours#How does this call it
                 #Finds the area of the object, contours
        area = cv2.contourArea(contour)
        if area > setUp.areaMin and area < setUp.areaMax:
            
           #Finds the permimeter of the object 
            perimeter = cv2.arcLength(contour, True)
            if perimeter > setUp.perimeterMin and perimeter < setUp.perimeterMax:
                
                '''edge number'''
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)jjjj
                if len(approx) == 6 or len(approx) == 7 or len(approx) == 8:

                    '''Diagaonal rectangle stuff'''
                    rect = cv2.minAreaRect(contour)
                    '''box = cv2.boxPoints(rect)
                    box = numpy.int0(box)
                    outImage = cv2.drawContours(origImage, [box], 0,(255,0,255), 3)'''
                    ((x, y), (oldW, oldH), r) = rect
                    if oldW < oldH:
                        w = oldH
                        h = oldW
                    else:
                        w = oldW
                        h = oldH
                    if h < setUp.maxHeight and w < setUp.maxWidth and h > setUp.minHeight and w > setUp.minWidth:

                        '''width/heigh ratio'''
                        if float(w)/float(h) < setUp.whRatioMax and float(w)/float(h) > setUp.whRatioMin:
    
                            
                            '''perimeter ratio'''
                            #print("yay 2")
                            if perimeter / (2*w + 2*h) < setUp.perimeterRatioMax and perimeter / (2*w + 2*h) > setUp.perimeterRatioMin:
                                contoursFinal.append([x,y,w,h, True, (w*h*-1)])
    contoursFinal.sort(key=lambda x: int(x[5]))
    return outImage, contoursFinal

    def makeNetworkTable(IP):
        NetworkTable.setIPAddress(IP)
        NetworkTable.setClientMode()
        NetworkTable.initialize()
        return NetworkTable.getTable("vision")

    def HSVthresholdSlider():
        stream = PiVideoStream().start()
    
        cv2.namedWindow('HSV threshold slider')
        cv2.createTrackbar('hLow', 'HSV threshold slider', 0, 180, nothing)
        cv2.createTrackbar('hHigh', 'HSV threshold slider', 0, 180, nothing)
        cv2.createTrackbar('sLow', 'HSV threshold slider', 0, 255, nothing)
        cv2.createTrackbar('sHigh', 'HSV threshold slider', 0, 255, nothing)
        cv2.createTrackbar('vLow', 'HSV threshold slider', 0, 255, nothing)
        cv2.createTrackbar('vHigh', 'HSV threshold slider', 0, 255, nothing)

    while(True):
        image = stream.read()
        cv2.imshow('HSV threshold slider', image)
        hLow = cv2.getTrackbarPos('hLow', 'HSV threshold slider')
        hHigh = cv2.getTrackbarPos('hHigh', 'HSV threshold slider')
        sLow = cv2.getTrackbarPos('sLow', 'HSV threshold slider')
        sHigh = cv2.getTrackbarPos('sHigh', 'HSV threshold slider')
        vLow = cv2.getTrackbarPos('vLow', 'HSV threshold slider')
        vHigh = cv2.getTrackbarPos('vHigh', 'HSV threshold slider')
        hsvLower = numpy.array([hLow, sLow, vLow])
        hsvUpper = numpy.array([hHigh, sHigh, vHigh])
        cv2.imshow("original", image)
        image = cv2.GassiunBlur(image, setUp.blur, 0)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image = cv2.inRange(image, hsvLower, hsvUpper)
        cv2.imshow("hsv", image)
        cv2.waitkey(0)
        break 

    def main():
        #HSVthresholdSlider()
        lastTime = 0

        #create NetworkTable, check the id for the RoboRio
        table = makeNetworkTable(VisionsetUpMap.roboRIOIP)
        table.putNumber("centerX", -1)
        table.putNumber("centerY", -1)
        table.putNumber("width", -1)
        table.putBoolean("Found", False)
        table.putBoolean("True" True)

        #Start stream
        stream = CameraStream().start()
        time.sleep(2)
        
        print("started")
        
        while(True):
            #startTime = time.time()
            image = stream.read()
            _, contours = processImage(image)
            try:
                table.putBoolean("Found", True)
                table.putNumber("centerX", (contours[0][0]-setUp.centerY)) #use y because camera rotated
                table.putNumber("centerY", (contours[0][1]-setUp.centerX)) #use x because rotated
                table.putNumber("width", contours[0][3]) 
                table.putNumber("length", contours[0][4])
                print("Pushed to NetworkTables")#data retrived 
                time.sleep(.1)
            except:
                table.putBoolean("Found", False)

    if __name__ == "__main__":
        main()