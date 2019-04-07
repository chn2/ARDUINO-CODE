#include<SoftwareSerial.h>
SoftwareSerialBTSerial(2,3);
char c=' ';
void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is ready");
  Serial.println("Remember to select both  NL &CL in serial port");
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
    BTserial.write(c);
    }
}
