from __future__ import division
from __future__ import print_function
import cv2
import numpy as np

#load image 
img = cv2.imread("sun1.jpg",0)
#e1 = cv2.getTickCount()
#print img[10,10,0]
#e2 = cv2.getTickCount()
#print e2-e1

ret, thresh =cv2.threshold(img, 250,255, cv2.THRESH_BINARY)
x,y = thresh.nonzero()

px = x.mean()
py = y.mean()
#draw center point
#thresh.itemset((px,py),0)
print(px, py)
#opening
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(50,50))
opening2 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel2)

x,y = opening.nonzero()
px = x.mean()
py = y.mean()
print(px, py)
x,y = opening2.nonzero()
px = x.mean()
py = y.mean()
print(px, py)


#display
cv2.imshow('th',thresh)
cv2.imshow('open', opening)
cv2.imshow('open2', opening2)

cv2.waitKey(0)
cv2.destroyAllWindows()
