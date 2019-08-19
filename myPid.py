import math
import numpy 


speed_kp = 10

class PID:

    def __init__(self):

        self.last_coordinate_x= 0
        
    def SPEED_PID(self,coordinate_x):  # 速度环

        speed = coordinate_x - self.last_coordinate_x
        bias = 0 - speed
        
        pwm = speed_kp * bias 
        if(pwm<100 and pwm >-100):  # 增加死区 微小变化 不产生控制量
            pwm = 0
        self.last_coordinate_x = coordinate_x

        print(pwm)
        
