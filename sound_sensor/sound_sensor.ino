#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#include <LcdBarGraphX.h>

LiquidCrystal_I2C lcd (0x27, 2, 1, 0, 4, 5, 6, 7);

LcdBarGraphX rjx(&lcd, 16, 0, 1);

int V = 0;
int Max = 700;

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

  //LCD setup

  lcd.setBacklightPin(3, POSITIVE); 
  lcd.setBacklight(HIGH);
  

  lcd.begin(16,2);
  lcd.print("AEA");

  delay(3000);
}

void loop() {
  rjx.drawValue(V, Max);
  lcd.setCursor(0, 0);
  lcd.print("Volume");
}
