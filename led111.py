from time import sleep
from RPi.GPIO import *
setwarnings(False)
setmode(BCM)
setup(18,OUT)
while True:
    output(18,HIGH)
    sleep(1)
    output(18,LOW)
    sleep(1)
