#include<SoftwareSerial.h>
SoftwareSerial BTSerial(3,2);
char c=' ';
void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is ready");
  Serial.println("nl&cl");
  BTSerial.begin(38400);
}
void loop() {
  if(BTSerial.available())
  {
    c=BTSerial.read();
    Serial.write(c);
  }
  if(Serial.available())
  {
    c=Serial.read();
    BTSerial.write(c);
    }
}
