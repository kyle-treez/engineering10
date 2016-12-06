#include <Adafruit_Sensor.h>

//Compass stuff
#include <Wire.h> //I2C Arduino Library
#define address 0x1E //0011110b, I2C 7bit address of HMC5883

// Ultrasonic sensors use digital ports and needs a trigger to get an echo
int rearUStrigger = 24; // rear Ultrasonic prox sensor trigger
int rearUSecho = 22; // rear Ultrasonic prox sensor echo

int frontUStrigger = 51; // front Ultrasonic prox sensor trigger
int frontUSecho = 50; // front Ultrasonic prox sensor echo

// Microphones use analog inputs
int fR_MIC = 0; // front right microphone
int fL_MIC = 1; // front left microphone
int rR_MIC = 3; // rear right microphone
int rL_MIC = 2; // rear left microphone

// Compass uses digital ports
int compData = 46; // Compass Data
int compClock = 47; // Compass Clock

// Remote controls use Pulse Wave Modulation digital outputs
int rcLR = 12; // Remote Control L&R port FORWARD
int rcFB = 11; // Remote Control F&B port FRONT STREERING

int divider = 0;

int check_fR_MIC = 0;
int check_fL_MIC = 0;
int check_rR_MIC = 0;
int check_rL_MIC = 0;

int check_compass = 1;

int check_ultrasonicF = 0;
int check_ultrasonicR = 0;

void setup() {
  Serial.begin(9600);
  pinMode(rearUStrigger,OUTPUT);
  pinMode(rearUSecho,INPUT);
  pinMode(frontUStrigger,OUTPUT);
  pinMode(frontUSecho,INPUT);

  pinMode(rcLR,OUTPUT);
  pinMode(rcFB,OUTPUT);

//Setting up Compass stuff
  Wire.begin();
  //Put the HMC5883 IC into the correct operating mode
  Wire.beginTransmission(address); //open communication with HMC5883
  Wire.write(0x02); //select mode register
  Wire.write(0x00); //continuous measurement mode
  Wire.endTransmission();
}

void loop() {
  //#################MICROPHONE START################
  /////////////////FRONT RIGHT///////////////////////
  if(check_fR_MIC == 1){
    for(int i = 0; i <=10; i++){
      int sample = analogRead(fR_MIC);
     Serial.println(sample);
    }
    Serial.println(divider);
  }
  /////////////////FRONT LEFT///////////////////////
  if(check_fL_MIC == 1){
    for(int i = 0; i <=10; i++){
      int sample = analogRead(fL_MIC);
     Serial.println(sample);
    }
    Serial.println(divider);
  }
  /////////////////REAR RIGHT///////////////////////
  if(check_rR_MIC == 1){
    for(int i = 0; i <=10; i++){
      int sample = analogRead(rR_MIC);
     Serial.println(sample);
    }
    Serial.println(divider);
  }
/////////////////REAR LEFT///////////////////////
  if(check_rL_MIC == 1){
    for(int i = 0; i <=10; i++){
      int sample = analogRead(rL_MIC);
     Serial.println(sample);
    }
    Serial.println(divider);
  }
  //#################MICROPHONE END#################

  //#################ULTRA SONIC START#################

  /////////////////FRONT ULTRASONIC PROX/////////////////
  if(check_ultrasonicF == 1){
    for(int i = 0; i <=10; i++){
      digitalWrite(frontUStrigger, LOW);
      digitalWrite(frontUStrigger, HIGH);
      digitalWrite(frontUStrigger, LOW);
      int duration = pulseIn(frontUSecho, HIGH);
      Serial.println(duration);
    }
    Serial.println(divider);
  }
  /////////////////REAR ULTRASONIC PROX/////////////////
  if(check_ultrasonicR == 1){
    for(int i = 0; i <=10; i++){
      digitalWrite(rearUStrigger , LOW);
      digitalWrite(rearUStrigger , HIGH);
      digitalWrite(rearUStrigger , LOW);
      int duration = pulseIn(rearUSecho , HIGH);
      Serial.println(duration);
    }
    Serial.println(divider);
  }
  //#################ULTRA SONIC END#################

  /////////////////CHECK COMPASS/////////////////
  if(check_compass == 1){
    for(int i = 0; i <=10; i++){
      int x,y,z; //triple axis data

      //Tell the HMC5883L where to begin reading data
      Wire.beginTransmission(address);
      Wire.write(0x03); //select register 3, X MSB register
      Wire.endTransmission();
  
 
      //Read data from each axis, 2 registers per axis
      Wire.requestFrom(address, 6);
      if(6<=Wire.available()){
        x = Wire.read()<<8; //X msb
        x |= Wire.read(); //X lsb
        z = Wire.read()<<8; //Z msb
        z |= Wire.read(); //Z lsb
        y = Wire.read()<<8; //Y msb
        y |= Wire.read(); //Y lsb
      }
  
      //Print out values of each axis
      Serial.print("x: ");
      Serial.print(x);
      Serial.print("  y: ");
      Serial.print(y);
      Serial.print("  z: ");
      Serial.println(z);
  
      delay(250);
    }
    Serial.println(divider);
  }

  /////////////////MOTOR TEST/////////////////
  analogWrite(rcLR,50);
  
}
