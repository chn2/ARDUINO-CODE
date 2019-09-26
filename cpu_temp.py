import time
while True:
    tfile=open("/sys/class/thermal/thermal_zone0/temp")
    temp=float(tfile.read())
    tempc=temp/1000
    print("cpu temparature is :",tempc)
    time.sleep(2)
