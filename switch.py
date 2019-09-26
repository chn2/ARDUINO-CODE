import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6,GPIO.OUT)
a=int(GPIO.input(5))

if a==1:
    GPIO.output(6,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(1)
else:
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.HIGH)
    time.sleep(1)
    
    
