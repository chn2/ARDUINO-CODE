import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
p=GPIO.PWM(19,40)
p.start(0)
while 1:
    for x in range(0,100):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    for x in range(100):
        p.ChangeDutyCycle(100-x)
        time.sleep(0.1)
            
        
    
     
    
