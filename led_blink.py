import RPi.GPIO as GPIO
import time
"""n=int(input("Enter the time: "))"""

for i in range(0,11):
    if(i%2==0):
        time.sleep(2)
        for j in range(0,i):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18,True)
            time.sleep(1)
            GPIO.output(18,False)
            time.sleep(1)
    
    
    
    
