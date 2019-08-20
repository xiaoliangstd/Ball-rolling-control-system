import math
import numpy 


speedy_kp = 15
speedx_kp = 15

speedy_kd = 20
speedx_kd = 20


positionx_kp = 0.07
positionx_kd = 0.02
positiony_kp = 0.07
positiony_kd = 0.02

class PID:

    def __init__(self):

        self.last_coordinate_y= 0
        self.last_coordinate_x= 0

        self.last_spped_y= 0
        self.last_spped_x= 0

        self.lastx_bias = 0
        self.lasty_bias = 0
        
        self.x_target = 267
        self.y_target = 252



    def SPEEDY_PID(self,coordinate_y,positiony_pwm):  # 速度环y

        speed = coordinate_y - self.last_coordinate_y
        bias = positiony_pwm+0 - speed
        #bias = 0 - speed
        bias = -bias # 反相
        pwm = speedy_kp * bias + speedy_kd * (speed - self.last_spped_y)
        '''
        if(pwm<120 and pwm >-120):  # 增加死区 微小变化 不产生控制量
            pwm = 0
        '''
        self.last_coordinate_y = coordinate_y
        self.last_spped_y = speed
        return pwm

    def SPEEDX_PID(self,coordinate_x,positionx_pwm):  # 速度环x

        speed = coordinate_x - self.last_coordinate_x
        
        bias = positionx_pwm+0 - speed
        #bias = 0 - speed
        bias = -bias
        pwm = speedx_kp * bias + speedx_kd * (speed - self.last_spped_x)
        '''
        if(pwm<120 and pwm >-120):  # 增加死区 微小变化 不产生控制量
            pwm = 0
        '''
        self.last_coordinate_x = coordinate_x
        self.last_spped_x = speed
        
        return pwm


    def POSITIONX_PID(self,positionx):
       
        if(positionx < self.x_target+5 and positionx >self.x_target-5):
            positionx = self.x_target
        
        bias = self.x_target - positionx

        pwm = positionx_kp*bias + positionx_kd * (bias - self.lastx_bias)
        self.lastx_bias = bias
        return pwm

    def POSITIONY_PID(self,positiony):
         
        if(positiony < self.y_target+5 and positiony > self.y_target-5):
            positiony = self.y_target
        
        bias = self.y_target - positiony
        pwm = positiony_kp*bias + positiony_kd * (bias - self.lasty_bias)
        self.lasty_bias = bias


        return pwm
        
