#include<Adafruit_Sensor.h>
#include"DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN,DHTTYPE);
const int trigPin=3;
const int echoPin=2;
long duration;
int distance;

void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 test!");
  dht.begin();
   pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
}

void loop() {
  delay(2000);
  float h=dht.readHumidity();
  float t=dht.readTemperature();
  Serial.print("Humidity:\t");
  Serial.print(h);
 Serial.print("%\n");
 delay(500);
 Serial.print("Temperature:\t");
 Serial.print(t);
 Serial.print("*C \n"); 
 digitalWrite(trigPin,LOW);
delayMicroseconds(2);
digitalWrite(trigPin,HIGH);
delayMicroseconds(10);
digitalWrite(trigPin,LOW);

duration=pulseIn(echoPin,HIGH);
distance=duration*0.034/2;
Serial.print("Distance:");
Serial.print(distance);
Serial.print("\n");
}
