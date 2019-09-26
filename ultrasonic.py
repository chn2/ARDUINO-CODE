import RPi.GPIO as x
import time
x.setwarnings(False)
x.setmode(x.BCM)
trig=5
echo=6
x.setup(trig,x.OUT)
x.setup(echo,x.IN)
while True:
    x.output(trig,1)
    time.sleep(0.000001)
    x.output(trig,0)
    starttime=0
    stoptime=0
    while(x.input(echo)==0):
        starttime+=1
    stoptime=starttime
    while(x.input(echo)==1):
        stoptime+=1
    T=stoptime - starttime
    dist=T * 0.0172
    print("distance= ",dist)
    time.sleep(1)
    
