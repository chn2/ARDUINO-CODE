import sys
import Adafruit_DHT
import http.client
import urllib
import time
key = 'V7ZQQIM33602CUZQ'
def dht():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
        a = temperature
        b=humidity
        params = urllib.parse.urlencode({'field1': a, 'field2': b,'key':key })
        headers = {"Content-typZZe": "application/x-www-formurlencoded","Accept":"text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
            break
    #sleep for desired amount of time
if __name__ == "__main__":
    
    while True:    
        dht()
        time.sleep(1)
