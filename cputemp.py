import http.client
import urllib
import time
sleep = 30 # how many seconds to sleep between posts to the channel
key = 'TBJ3E9AEPV8GV7VW' # Thingspeak channel to update
#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer():
 while True:
 #Calculate CPU temperature of Raspberry Pi in Degrees C
     temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU
#temp
     params = urllib.parse.urlencode({'field2': temp, 'key':key })
     headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
     conn = http.client.HTTPConnection("api.thingspeak.com:80")
 
     try:
         conn.request("POST", "/update", params, headers)
         response = conn.getresponse()
         print (temp)
         print (response.status, response.reason)
         data = response.read()
         conn.close()
     except:
         print ("connection failed")
         break
#sleep for desired amount of time
if __name__ == "__main__":
     while True:
         thermometer()
         time.sleep(sleep)