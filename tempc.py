import time
while True:
    cfile=open("/sys/class/thermal/thermal_zone0/temp")
    temp=float(cfile.read())
    tempc=temp/1000
    print("cpu temp is", tempc)
    time.sleep(2)
