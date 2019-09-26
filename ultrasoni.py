import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=18
while True:
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    GPIO.setup(12,GPIO.OUT)
    print("waiting for sensor to settle")
    time.sleep(2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        T1=time.time()
        GPIO.output(12,GPIO.LOW)
        
    while GPIO.input(ECHO)==1:
        T2=time.time()
        GPIO.output(12,GPIO.HIGH)
    Tt=T2-T1
    distance=Tt*172
    distance=round(distance,2)
    print("distance",distance,"cm")
