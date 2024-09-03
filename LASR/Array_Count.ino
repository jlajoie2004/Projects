String message;
int count = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()>0)
  {
    message = Serial.readString();
    count++;
    Serial.print(message); // just for testing purposes
    Serial.print(count); 
  }

}
