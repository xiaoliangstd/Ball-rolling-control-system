import serial
import time
ser = serial.Serial('/dev/ttyUSB0',115200)


def sendx_angle(angle):

    angle = 1000 + int(angle)
    angle = str(angle)

    angle = str(angle)
    send_angle = "#1P"+angle+"T70\r\n"
    print(angle)
    ser.write(send_angle.encode())

def sendy_angle(angle):

    angle = 1932 + int(angle)
    angle = str(angle)
    send_angle = "#0P"+angle+"T70\r\n"
    #print(angle)
    ser.write(send_angle.encode())



if __name__ == "__main__":
    while True:
        sendx_angle(1000)
        time.sleep(0.1)
        sendy_angle(1932)
        time.sleep(1)
        sendx_angle(1000)
        time.sleep(0.1)
        sendy_angle(1932)
        time.sleep(1)