import RPi.GPIO as x
import time
x.setwarnings(False)
x.setmode(x.BCM)
trigger=18
echo=24
x.setup(trigger,x.OUT)
x.setup(echo,x.IN)
while True:
    x.output(trigger,x.HIGH)
    time.sleep(0.00001)
    x.output(trigger,x.LOW)
    starttime=time.time()
    stoptime=time.time()
    while(x.input(echo)==0):
        starttime=time.time()
    while(x.input(echo)==1):
        stoptime=time.time()
    totaltime=stoptime-starttime
    distance=(totaltime*34300)/2
    print("distance is:",distance)
    time.sleep(1)
    
