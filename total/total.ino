
#include <Servo.h>
Servo servo;
int pos=0,number=0;
int trigg=8,echo=7;
const float speed_sound=0.034;

void setup() {
 pinMode(trigg,OUTPUT);
pinMode(echo,INPUT);
servo.attach(9);
Serial.begin(9600);
}

float distance(){
  unsigned long duration; 
  float n_distance;
  digitalWrite(trigg,LOW);
delayMicroseconds(2);
digitalWrite(trigg,OUTPUT);
delayMicroseconds(10);
digitalWrite(trigg,LOW);
duration=pulseIn(echo,HIGH);
n_distance=duration*speed_sound/2;
return(n_distance);
}

void loop() {
String nb;
int angle;
float dist;
for(angle=0;angle<=180;angle++){
servo.write(angle);
dist=distance();
Serial.print(angle);
Serial.print(";");
Serial.println(dist);
delay(50);
}
for(angle=180;angle>=0;angle--){
servo.write(angle);
dist=distance();
Serial.print(angle);
Serial.print(";");
Serial.println(dist);
delay(50);
}
}
