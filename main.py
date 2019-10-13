import cv2 as cv  
import numpy as np 
import serial
import time
from control import PID
from servo import sendy_pwm
from servo import sendx_pwm

ser = serial.Serial('/dev/ttyUSB0',115200)
kernel = np.ones((5,5),np.uint8)
cap = cv.VideoCapture(1)
lower = np.array( [147, 127 , 46])
upper = np.array([171 ,228, 103])

pid = PID()
i = 0


while True:

    ret,img = cap.read()
    canvas = np.copy(img)
    canvas1 = np.copy(img)
    img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    img = cv.inRange(img,lower,upper)
    img = cv.medianBlur(img,5) 
    edges = cv.dilate(img, kernel, iterations=2)
    cv.imshow("edges",edges)
    contours, hier = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
            x,y,w,h = cv.boundingRect(cnt)
            area = w*h
            x = x # 补偿
            #y = y-5
            if area > 1000 and area < 5000:
                x_cen = int(x+w/2)
                y_cen = int(y+h/2)
                print("x:",x_cen,"y:",y_cen) 
                canvas = cv.rectangle(canvas,(x,y),(x+w,y+h),(255,255,0),3) 
                px = pid.POSITIONX_PID(x_cen)
                py = pid.POSITIONY_PID(y_cen)
                pwmy = pid.SPEEDY_PID(y_cen,px) 
                pwmx = pid.SPEEDX_PID(x_cen,py) 
                sendx_pwm(pwmx)
                cv.waitKey(1)
                sendy_pwm(pwmy)
                
    cv.imshow("canvas",canvas)
    key_num = cv.waitKey(4)
    # 切换位置点
    if key_num == ord("q"):
        pid.x_target = 280
        pid.y_target = 252

    if key_num == ord("w"):
        pid.x_target = 410
        pid.y_target = 410

    if key_num == ord("e"):
        pid.x_target = 130
        pid.y_target = 370

    if key_num == ord("r"):
        pid.x_target = 160
        pid.y_target = 110

    if key_num == ord("t"):
        pid.x_target = 440
        pid.y_target = 120

    if key_num == ord("s"):
        cv.imwrite("sucai.png",canvas1)
        break

cap.release()
cv.destroyAllWindows()