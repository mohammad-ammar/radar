#include <Servo.h>
Servo servo;
int pos=0;
int number=0;
void setup() {
servo.attach(9);
Serial.begin(9600);
}

void loop() {
String nb;
int angle;
for(angle=0;angle<=180;angle++){
servo.write(angle);
Serial.println(angle);
}
for(angle=180;angle>=0;angle--){
servo.write(angle);
Serial.println(angle);
}
}
