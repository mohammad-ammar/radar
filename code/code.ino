int trigg=8,echo=7;
const float speed_sound=0.034; // 3402.9 cm/us
void setup() {
pinMode(trigg,OUTPUT);
pinMode(echo,INPUT);
Serial.begin(9600);
}

void loop() {
unsigned long duration; // duration of sound 
float distance;
digitalWrite(trigg,LOW);
delayMicroseconds(2);
digitalWrite(trigg,OUTPUT);
delayMicroseconds(10);
digitalWrite(trigg,LOW);
duration=pulseIn(echo,HIGH);
distance=duration*speed_sound/2;

Serial.println(distance);
}
