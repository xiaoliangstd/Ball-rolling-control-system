import serial
import time
ser = serial.Serial('/dev/ttyUSB0',115200)

def sendx_pwm(angle):

    angle = 1000 + int(angle)
    angle = str(angle)
    send_angle = "#1P"+angle+"T70\r\n" # 该串口总线舵机协议
    ser.write(send_angle.encode())

def sendy_pwm(angle):

    angle = 1932 + int(angle)
    angle = str(angle)
    send_angle = "#0P"+angle+"T70\r\n" # 该串口总线舵机协议
    ser.write(send_angle.encode())


if __name__ == "__main__":
    
    pass
      