from __future__ import print_function
from __future__ import division
import time
import picamera
import picamera.array
import cv2
import numpy as np
from fractions import Fraction
from datetime import datetime
import math

def pyCamConfig(camera, exposure='off', awb_mode= 'off', iso=1000,sSpeed=4000):
    '''config pycam'''
    camera.exposure_mode = exposure
    camera.awb_mode = awb_mode
    camera.iso = iso
    camera.shutter_speed= sSpeed

def myfilter(image, kernel):
    '''filter the image'''
    return cv2.morphologyEx(image ,cv2.MORPH_OPEN, kernel)
    #return cv2.morphologyEx(image ,cv2.MORPH_CLOSE, kernel)
    #return cv2.erode(image, kernel)

def meanXY(image):
    x,y = image.nonzero()
    try:
        return(int(x.mean()), int(y.mean()))
    except ValueError:
        return(None,None)
#file
myfile = open('solar.cca','w')
#pos vars
tmpX = None
tmpY = None
mx = None
my = None
#kernel
size=3
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(size, size))
#var definition
thVal = 250
picSize = (640,480)
framerate = 60
fillvalue = 255
#camera config values
myIso= 1600
myspeed = 5000
#mask for floodfill
mask = np.zeros((picSize[1]+2,picSize[0]+2), np.uint8)
frec = cv2.getTickFrequency()
with picamera.PiCamera(resolution=picSize, framerate=framerate) as camera:
    camera.vflip = True
    pyCamConfig(camera, iso=myIso, sSpeed= myspeed)
    #initial date
    date0=datetime.now()
    while(True):
        with picamera.array.PiRGBArray(camera) as stream:
            e0 = cv2.getTickCount()
            #e1 = e0
            #get image
            print('get ', end=' ')

            camera.capture(stream,
                format='bgr',
                )
            image = stream.array
            #resize
            #image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            #print(image.shape)
            #e2 = cv2.getTickCount()
            #print ((e2-e1)/frec, end=' ')
            #e1 = e2 
            #transform
            HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            H,S,V = cv2.split(HSV)
            #print('convert ', end=' ')
            #e2 = cv2.getTickCount()
            #print ('{:f}'.format((e2-e1)/frec), end=' ' )
            #e1 = e2
            ret, resimage =cv2.threshold(V,
                            thVal,
                            fillvalue,
                            cv2.THRESH_BINARY,
                            )
            #e2 = cv2.getTickCount()
            #print('th ', end=' ' )
            #print ((e2-e1)/frec, end=' ' )
            #e1 = e2
            #filter
            resimage = myfilter(resimage, kernel)
            #print('filter', end=' ' )
            #e2 = cv2.getTickCount()
            #print ((e2-e1)/frec, end=' ' )
            #e1 = e2
            #mean
            mx, my = meanXY(resimage)
            #print('mean', end=' ' )
            #e2 = cv2.getTickCount()
            #print ((e2-e1)/frec, end=' ')
            print ('pos:',mx,my)
            date1=datetime.now()
            if mx != None and tmpX!=None:
                cv2.line(resimage,(0,mx),(picSize[0],mx), 255)
                cv2.line(resimage,(my,0),(my, picSize[1]), 255)
                tmpX-=mx
                tmpY-=my
                d = math.sqrt(tmpX*tmpX+tmpY*tmpY)
                interv = date1-date0
                speed = d/interv.total_seconds()
                wStr=str(date1)+','+str(mx)+','+str(my)+','+str(speed)+'\n'
            else:
                wStr = str(date1)+',NAN,NAN,NAN,\n'
            tmpX = mx
            tmpY = my
            #show
            cv2.imshow('umbral', resimage)
            cv2.imshow('image', image)
            e2 = cv2.getTickCount()
            totalT=(e2-e0)/frec
            key = cv2.waitKey(1) & 0xFF 
            if key == ord('q'):
                break
            elif key == ord('e'):
                thVal+=5
            elif key == ord('w'):
                thVal-=5
            elif key == ord('s'):
                myspeed -= 500
            elif key == ord('d'):
                myspeed += 500
            elif key == ord('x'):
                myIso -= 100
            elif key == ord('c'):
                myIso += 100
            print('pTime:',totalT,'TH:',thVal, 'Ss:', myspeed, 'ISO:', myIso)
            print(wStr)
            myfile.write(wStr)
            time.sleep(1)
myfile.close()
