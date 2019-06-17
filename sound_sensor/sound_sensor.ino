void setup() {
  // Variable declaration
  int cont = 1;
  
  
  // initialize serial comunication at 9600 bits per second
  Serial.begin(9600);

  while (cont <= 400){
    //read the input on analof pin 0
    int V = analogRead(A0);
    //Print second and Hz value
    //Serial.println(seg);
    Serial.println(V);
    delay(5);
    cont++;
  }
  Serial.println("Read finished");
}

void loop() {
  // put your main code here, to run repeatedly:

}
