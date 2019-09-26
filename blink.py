import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)

while True:
    GPIO.output(18,1)
    time.sleep(2)
    GPIO.output(18,0)
    time.sleep(1)
