import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.IN)
try:
    while True:
        x=GPIO.input(21)
        if(x==1):
            print('object Detected')
            t.sleep(1)
        else:
            print('LOVELY')
            t.sleep(1)
except keyboardInterrupt:
    print('User interrupted')
    GPIO.cleanup()
