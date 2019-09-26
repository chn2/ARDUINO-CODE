import RPi.GPIO as GPIO
import time
while True:
           GPIO.setmode(GPIO.BCM)
           GPIO.setwarnings(False)
           GPIO.setup(18,GPIO.IN)
           
           GPIO.output(18,GPIO.HIGH)
           time.sleep(2)
           GPIO.output(18,GPIO.LOW)
           time.sleep(2)
