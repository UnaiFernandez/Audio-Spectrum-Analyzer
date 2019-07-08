#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>


LiquidCrystal_I2C lcd (0x27, 2, 1, 0, 4, 5, 6, 7);

byte customchar[8] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111 
};

byte R_peak[8] = {
  B00000,
  B00000,
  B00011,
  B00111,
  B00000,
  B00000,
  B00000,
  B00000
};

byte R_head[8] = {
  B00000,
  B01110,
  B11011,
  B11111,
  B01111,
  B00111,
  B01111,
  B11111
};

byte R_tail[8] = {
  B11111,
  B11111,
  B11111,
  B01111,
  B00111,
  B01110,
  B11000
};

byte R_back1[8] = {
  B00000,
  B00000,
  B00000,
  B10000,
  B11000,
  B11100,
  B11100,
  B11100
};

byte R_back2[8] = {
  B11100,
  B11100,
  B10100,
  B10100,
  B01000,
  B00000,
  B00000,
  B00000
};
int V = 0;
int Max = 400;

void setup() {
  // Variable declaration
  int cont = 1;
  int k = 1;
  //LCD setup
  lcd.begin(16,2);
  lcd.setBacklightPin(3, POSITIVE); 
  lcd.setBacklight(HIGH);
  lcd.createChar(0, R_peak);
  lcd.createChar(1, R_head);
  lcd.createChar(2, R_tail);
  lcd.createChar(3, R_back1);
  lcd.createChar(4, R_back2);  
  lcd.createChar(5, customchar);
  //lcd.home(); 
  raven(0,1);
  lcd.setCursor(4, 0);
  lcd.print("RAVEN");

  delay(1000);

  lcd.clear();
  // initialize serial comunication at 9600 bits per second
  Serial.begin(9600);
  lcd.setCursor(0, 0);
  lcd.print("Reading data...");
  lcd.setCursor(0, 1);
  while (cont <= Max){
    //read the input on analof pin 0
    int V = analogRead(A0);
    //Print second and Hz value
    //Serial.println(seg);
    Serial.println(V);
    delay(5);
    cont++;
    if(cont%25 == 0&& k <= 16){
      lcd.write(byte(5));
      k++;
    }
  }
  Serial.println("Read finished");
  lcd.setCursor(0, 0);
  lcd.clear();
  lcd.print("Read finished");
  raven(13, 14);
  lcd.print("RAVEN");
  delay(1000);

  for (int i = 0; i<13; i++){
    lcd.scrollDisplayLeft();
    delay(150);
  }

}

void loop() {
  
}

void raven(int a, int b){
 lcd.setCursor(a, 0);
 lcd.write(byte(0));
 lcd.write(byte(1));
 lcd.write(byte(3));
 lcd.setCursor(b, 1);
 lcd.write(byte(2));
 lcd.write(byte(4));
}
