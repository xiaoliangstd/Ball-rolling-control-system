import math
import numpy 
import serial
ser = serial.Serial('/dev/ttyUSB0',115200)
class PID():

    def __init__(self):
        
        self.kp_x = 1.1
        self.ki_x = 0
        self.kd_x = 9
        self.kp_y = 1.1
        self.ki_y = 0
        self.kd_y = 9
        
        self.x_target = 355
        self.y_target = 335

        self.last_bias_x = 0
        self.intergral_bias_x = 0
        
        self.last_bias_y = 0
        self.intergral_bias_y = 0

        self.pwm_y = 0
        self.pwm_x = 0

    def pid_x(self,coordinate_x):

        bias = self.x_target -  coordinate_x
        self.intergral_bias_x += bias
        self.pwm_x = self.kp_x*bias + self.ki_x*self.intergral_bias_x + self.kd_x*(bias - self.last_bias_x)
        self.last_bias_x = bias 
        


    def pid_y(self,coordinate_y):
        
        bias = coordinate_y  - self.y_target
        self.intergral_bias_y += bias
        self.pwm_y = self.kp_y*bias + self.ki_y*self.intergral_bias_x + self.kd_y*(bias - self.last_bias_y)
        self.last_bias_y = bias 
        

    def print_pwm(self):
        print("pwmx:",self.pwm_x,"pwmy:",self.pwm_y)

    def send_pwm(self): 
        servo1 = 1000  # x servo
        servo2 = 1000  # y servo 
        
        if self.pwm_x >0:
            servo1 = int(servo1 + self.pwm_x)

        if self.pwm_x <0:
            servo1 = int(servo1 + self.pwm_x)

        if servo1 < 900:
            servo1 = 900
        if servo1 > 1100:
            servo1 = 1100

        if servo1 <1000:
            servo1 = '0'+str(servo1)
        else:
            servo1 = str(servo1)


        if self.pwm_y >0:
            servo2 = int(servo2 + self.pwm_y)

        if self.pwm_y <0:
            servo2 = int(servo2 + self.pwm_y)

        if servo2 < 900:
            servo2 = 900
        if servo2 > 1100:
            servo2 = 1100
        
        if servo2 < 1000:
            servo2 = '0'+str(servo2)
        else:
            servo2 = str(servo2)
       
        

        # if self.pwm_x >0:


        #     bbb = "1000"+ "1100"
        # if self.pwm_x <0:

        #     bbb = "1000"+ "0900"
        

        bbb = servo2+ servo1
        print(bbb)
        ser.write(bbb.encode())
        
        



    

