import RPi.GPIO as GPIo
import time
GPIo.setmode(GPIo.BCM)
GPIo.setwarnings(False)
GPIo.setup(19,GPIo.OUT)
    
while 1:
    if(x==0):
        print("NO OBJECTIS DETECTED")
        GPIo.output(19,GPIo.LOW)
        time.sleep(0.2)

    else:
        print("objectisdetected")
        GPIo.output(19,GPIo.HIGH)
        time.sleep(0.2)

        
