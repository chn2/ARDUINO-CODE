int CommonAnode[]={0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x38,0x00,0x10,0x08,0x00,0x46,0x40,0x06,0x0E};
int CommonAnode2[]={0x40,0x79,0x24,0x30,0x19,0x12,0x02,0x38,0x00,0x10,0x08,0x00,0x46,0x40,0x06,0x0E};
void setup() {

DDRD=B1111111;
DDRB=B1111111;
}

void loop() {
 
 for(int i=0;i<16;i++)
 {
  PORTD=CommonAnode[i];
  for(int j=0;j<16;j++)
  {
 PORTB=CommonAnode[j];
  
  delay(1000);
 }
 }
}