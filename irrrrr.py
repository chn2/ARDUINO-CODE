import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
while(True):
    if (GPIO.output(18)==True):
        
        time.sleep(0.5)
        print("Detected");
    
    if (GPIO.output(18)==False):
        time.sleep(0.5)
        print("not detected");
