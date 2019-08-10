import math
import numpy 
import serial
#ser = serial.Serial('/dev/ttyUSB0',115200)
class PID():

    def __init__(self):
        
        self.kp_x = 0.9
        self.ki_x = 0
        self.kd_x = 10
        self.kp_y = 5
        self.ki_y = 0
        self.kd_y = 0
        
        self.x_target = 355
        self.y_target = 335

        self.last_bias_x = 0
        self.intergral_bias_x = 0
        
        self.last_bias_y = 0
        self.intergral_bias_y = 0

        self.pwm_y = 0
        self.pwm_x = 0

    def pid_x(self,coordinate_x):

        if coordinate_x >345 and coordinate_x < 365:
            coordinate_x = 355

        bias = self.x_target -  coordinate_x
        self.intergral_bias_x += bias
        self.pwm_x = self.kp_x*bias + self.ki_x*self.intergral_bias_x + self.kd_x*(bias - self.last_bias_x)
        self.last_bias_x = bias 
        


    def pid_y(self,coordinate_y):
        
        if coordinate_y >325 and coordinate_y < 345:
            coordinate_y = 335


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

        if servo1 < 850:
            servo1 = 850
        if servo1 > 1150:
            servo1 = 1150

        if servo1 <1000:
            servo1 = '0'+str(servo1)
        else:
            servo1 = str(servo1)


        if self.pwm_y >0:
            servo2 = int(servo2 + self.pwm_y)

        if self.pwm_y <0:
            servo2 = int(servo2 + self.pwm_y)

        if servo2 < 850:
            servo2 = 850
        if servo2 > 1150:
            servo2 = 1150
        
        if servo2 < 1000:
            servo2 = '0'+str(servo2)
        else:
            servo2 = str(servo2)
       
        

        # if self.pwm_x >0:


        #     bbb = "1000"+ "1100"
        # if self.pwm_x <0:

        #     bbb = "1000"+ "0900"
        

        bbb = servo2+ '1000'
        print(bbb)
        #ser.write(bbb.encode())
        
        



    

