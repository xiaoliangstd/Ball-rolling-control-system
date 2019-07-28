import numpy as np 
import matplotlib.pyplot as plt

kp = 2
ki = 2
kd = 6

encode = None

intergral_bias = 0
last_bias = 0

def pid(encode,Target):
    global intergral_bias
    global kp
    global ki 
    global kd 
    global last_bias

    bias = Target - encode 
    intergral_bias += bias
    pwm = kp*bias + ki*intergral_bias+kd*(bias - last_bias)
    last_bias = bias

    return pwm


if __name__ == "__main__":


    i = 0
    encode_recode = []
    encode = 0
    while True:

        Target = 200
        pwm = pid(encode,Target)
        encode += pwm*0.1
        encode_recode.append(encode)
        i+=1
        
        if i ==200:
            #print(encode_recode)
            break
    plt.plot(encode_recode)
    plt.show()    

