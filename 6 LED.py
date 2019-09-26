import RPi.GPIO as GPIO
import time
x=int(input("enter x: "))
for x in range(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(18,GPIO.LOW)
    time.slepp(3)
