import RPi.GPIO as x
import time
c=int(input("enter the no:"))
x.setwarnings(False)
x.setmode(x.BCM)
x.setup(19,x.OUT)
p=x.PWM(19,100)
p.start(10)
while 1:
    for s in range (c):
        p.ChangeDutyCycle(s)
        time.sleep(0.1)

    for s in range (c):
        p.ChangeDutyCycle(c-s)
        time.sleep(0.1)
