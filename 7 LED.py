import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
GPIO.output(17,GPIO.HIGH)
time.sleep(2)
GPIO.output(18,GPIO.HIGH)N
GPIO.output(17,GPIO.LOW)
time.sleep(3)
GPIO.output(18,GPIO.HIGH)
GPIO.output(17,GPIO.HIGH)
time.sleep(4)
GPIO.cleanup()
