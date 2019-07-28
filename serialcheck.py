import numpy as np 
import serial
import time

# 舵机调试代码
ser = serial.Serial('/dev/ttyUSB0',115200)
while True:

  a = input('servo1\n')
  b = input('servo2\n')



 
  bbb = a + b
  ser.write(bbb.encode())