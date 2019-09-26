import RPi.GPIO as x
import time
x.setmode(x.BCM)
x.setup(18,x.IN)
while True:
    Y=int(x.input(18))
    if(Y==1):
        print("OBJECT DETECTED")
        time.sleep(1)
    else:
        print("OBJECT  NOT DETECTED")
        time.sleep(1)
       
