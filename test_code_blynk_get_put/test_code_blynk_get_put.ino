#define BLYNK_PRINT Serial
#include<ESP8266WiFi.h>
#include<BlynkSimpleEsp8266.h>

BlynkTimer timer;
WidgetLCD BLYNK_LCD(V0); 

char auth[] = "40fd56944e544373a43c8c1c8820f2eb";//bharath 9059191902
char ssid[] = "CHINTU";
char pass[] = "chintu345";
int LED =D0;//D1


BLYNK_WRITE(V1)
{
  int LED_VAL = param.asInt(); // assigning incoming value from pin V1 to a variable
  if(LED_VAL==HIGH)
  {
    digitalWrite(LED,HIGH);
    BLYNK_LCD.print(0,1,"LED ON");
    delay(10);
    }
   else
   {
    //lcd.clear();
    digitalWrite(LED,LOW);
    BLYNK_LCD.print(0,1,"LED OFF");
    delay(10); 
    }
    
}


void READ_SENSOR()
{
  int POT=analogRead(A0);
  POT=POT;
  Blynk.virtualWrite(V2, POT);
  BLYNK_LCD.print(0,0,"POT:");
  BLYNK_LCD.print(5,0,POT);
    
}

void setup()
{
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  pinMode(LED,OUTPUT);//D0 pin of NodeMCU
  timer.setInterval(1000L,READ_SENSOR);//// change
}

void loop()
{
  Blynk.run();
  timer.run(); // Initiates BlynkTimer
}
