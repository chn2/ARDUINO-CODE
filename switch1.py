import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(16,GPIO.IN)
a=int(GPIO.input(16))

if a==1:
    
    GPIO.output(26,GPIO.HIGH)
   
else:
    GPIO.output(26,GPIO.LOW)
    
