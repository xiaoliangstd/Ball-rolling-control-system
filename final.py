import cv2 as cv  
import numpy as np 
import serial
import time
from myPid import PID
kernel = np.ones((5,5),np.uint8)
cap = cv.VideoCapture(1)
lower = np.array( [144,164,73])
upper = np.array([226,245,163] )

pid = PID()

while True:

    ret,img = cap.read()
    canvas = np.copy(img)
    img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    img = cv.inRange(img,lower,upper)
    img = cv.medianBlur(img,5) 
    edges = cv.dilate(img, kernel, iterations=2)
    cv.imshow("edges",edges)
    contours, hier = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
            x,y,w,h = cv.boundingRect(cnt)
            area = w*h
            x = x-10 # 补偿
            #y = y-5
            if area > 1000 and area < 5000:
                x_cen = int(x+w/2)
                y_cen = int(y+h/2)
                #print("x:",x_cen,"y:",y_cen)  
                pid.SPEED_PID(x_cen) 
                canvas = cv.rectangle(canvas,(x,y),(x+w,y+h),(255,255,0),3)
    cv.imshow("canvas",canvas)
    key_num = cv.waitKey(1)
    if key_num == ord("s"):
        cv.imwrite("sucai.png",canvas)
        break


cap.release()
cv.destroyAllWindows()