from RPi.GPIO import *
from time import sleep,time
setwarnings(False)
setmode(BCM)
trigger=5
echo=6
setup(trigger,OUT)

setup(echo,IN)
while True:
    output(trigger,True)
    sleep(0.00001)
    output(trigger,False)
    #sleep(1)
    starttime=time()
    stoptime=time()
    while (input(echo)==0):
        starttime=time()
    #print(starttime)
    while (input(echo)==1):
        stoptime=time()
    totaltime=stoptime-starttime
    distance=(totaltime*34300)/2
    print(distance)
    sleep(2)
