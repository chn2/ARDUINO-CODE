import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
a=int(input("enetr the delay time"))
for i in range(0,10):
    GPIO.output(18,GPIO.HIGH)
    time.sleep(a)
    GPIO.output(18,GPIO.LOW)
    time.sleep(a)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(a)
    GPIO.output(17,GPIO.LOW)
    time.sleep(a)
