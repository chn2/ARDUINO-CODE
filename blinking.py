import RPi.GPIO as a
import time
a.setwarnings(False)
a.setmode(a.BCM)
a.setup(19,a.OUT)
p=a.PWM(19,200)
p.start(0)
n=int(iput("enter the choice")
switch n:
    for x in range(0,99,1):
        p.ChangeDutyCycle(x)
        time.sleep(1)
    for x in range(99,0,-1):
        p.ChangeDutyCycle(x)
        time.sleep(1)
    
