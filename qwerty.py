import RPi.GPIO as GPIO
import time

#Setting GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.OUT)

#reading / writing gpio
while (True):
    x=GPIO.input(20)
    if (x == True):
        GPIO.output(21,True)
        time.sleep(0.2)
        print("Button pressed")
    else:
        GPIO.output(21,False)
        time.sleep(0.2)
        print("Button not pressed")
    
    
    
