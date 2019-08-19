import cv2 as cv  
import numpy as np 
import serial
from pid import PID 
import time
Pid = PID()

#ser = serial.Serial('/dev/ttyUSB0',115200)




def think(top_right,top_left,botto_left,botto_right,last_top_right,last_top_left,last_botto_left,last_botto_right):
    global src
    global error
    bias1 = abs(abs(top_right[0,0]-last_top_right[0,0])+abs(top_right[0,1]-last_top_right[0,1]))
    bias2 = abs(abs(top_left[0,0]-last_top_left[0,0])+abs(top_left[0,1]-last_top_left[0,1]))
    bias3 = abs(abs(botto_left[0,0]-last_botto_left[0,0])+abs(botto_left[0,1]-last_botto_left[0,1]))
    bias4 = abs(abs(botto_right[0,0]-last_botto_right[0,0])+abs(botto_right[0,1]-last_botto_right[0,1]))

    if bias1 >20 or bias2 >20 or bias3 >20 or bias4 >20:
        top_right = last_top_right
        top_left = last_top_left
        botto_left = last_botto_left
        botto_right = last_botto_right
        error = 1

    src = np.float32([top_left,top_right,botto_left,botto_right])
 




lower = np.array( [ 17, 167,  39])
upper = np.array([ 41, 255, 168] )

# lower = np.array(  [0, 0, 0])
# upper = np.array([ 86 ,163 , 53]   )
kernel = np.ones((5,5),np.uint8)
cap = cv.VideoCapture(1)
kernel = cv.getStructuringElement(cv.MORPH_CROSS,(9,9))
dst = np.float32([[0,0],[0,700],[700,0],[700,700]])
a = 0
error = 0   # 设置错误标志变量 如果错误则调用之前的信息
while True:

    ret,img = cap.read()
    canvas = np.copy(img)
    canvas1 = np.copy(img)
    cv.imshow("img",img)
    cv.waitKey(1)
    '''
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(img,5) 
    edges = cv.Canny(gray, 20, 90, apertureSize = 3)
   
    edges = cv.dilate(edges, kernel, iterations=1)

    contours, hier = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        area = w*h
        if  area > 120000 :
            epsilon = 0.1*cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,epsilon,True)
            try:
                top_right = approx[2]
                top_left = approx[3]
                botto_left = approx[0]
                botto_right = approx[1]
                if a == 0:   # 刚开始 设置过去变量  等异常时用

                    last_top_right = top_right
                    last_top_left = top_left
                    last_botto_left = botto_left
                    last_botto_right = botto_right
                    a +=1
                
                think(top_right,top_left,botto_left,botto_right,last_top_right,last_top_left,last_botto_left,last_botto_right)

                if error == 0:
                    last_top_right = top_right
                    last_top_left = top_left
                    last_botto_left = botto_left
                    last_botto_right = botto_right
                error = 0

            except IndexError:
                src = np.float32([last_top_left,last_top_right,last_botto_left,last_botto_right])
                error = 1

            M = cv.getPerspectiveTransform(src,dst)
            img = cv.warpPerspective(canvas1,M,(700,700))
            img = cv.flip(img,0)
            canvas3 = np.copy(img)
            img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
            img = cv.inRange(img,lower,upper)
            erosion = cv.erode(img,kernel,iterations = 1)
            dilation = cv.dilate(erosion,kernel,iterations = 2)
            cv.imshow("ddddd",dilation)
            contours,hierarchy = cv.findContours(dilation,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                x,y,w,h = cv.boundingRect(cnt)
                area = w*h
                if area > 1000 :
                    x_cen = int(x+w/2)
                    y_cen = int(y+h/2)
                    #print("x:",x_cen,"y:",y_cen)
                    
                    canvas = cv.rectangle(canvas3,(x,y),(x+w,y+h),(255,255,0),3)
                    #Pid.pid_x(x_cen) 
                    #Pid.pid_y(y_cen)
                    #Pid.print_pwm()  
                    #Pid.send_pwm()
                    
                    # 数据 格式 
                    if x_cen < 100 or y_cen < 100:
                        if  x_cen < 100 and y_cen < 100:
                            x_cen = '0' + str(x_cen)
                            y_cen = '0' + str(y_cen)

                        else:
                            if x_cen <100 :
                                x_cen = '0' + str(x_cen)
                                y_cen = str(y_cen)
                            else  :
                                x_cen = str(x_cen)
                                y_cen = '0' + str(y_cen)
                    else:

                        x_cen =  str(x_cen)
                        y_cen =  str(y_cen)
                    


                    coordinate = x_cen+y_cen 
                    print(coordinate)
                    #ser.write(coordinate.encode())
                    

    cv.imshow("canvas",canvas3)
    key = cv.waitKey(5)
    if key == ord('s'):
        cv.imwrite("sucai.png",canvas3)
        ser.write("10001000".encode())
        break
    '''
cap.release()
cv.destroyAllWindows()
