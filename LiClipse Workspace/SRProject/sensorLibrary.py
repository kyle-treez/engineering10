#!/usr/bin/python
from nanpy import Arduino
from nanpy import serial_manager
from time import sleep
import smbus
import time
import math

# Microphones use analog inputs
fR_MIC = 0 # front right microphone
fL_MIC = 1 # front left microphone
rR_MIC = 3 # rear right microphone
rL_MIC = 2 # rear left microphone

#Ultrasonic sensors use digital ports and needs a trigger to get an echo
rearUStrigger = 24 #rear Ultrasonic proximity sensor trigger
rearUSecho = 22 #rear Ultrasonic proximity sensor echo

frontUStrigger = 51  #front Ultrasonic proximity sensor trigger
frontUSecho = 50 #front Ultrasonic proximity sensor echo

#Compass uses digital ports
compData = 20; # Compass Data
compClock = 21 # Compass Clock

#Remote controls use Pulse Wave Modulation digital outputs
rcLR = 6 #Remote Control L&R port FRONT STREERING
rcFB = 7 #Remote Control F&B port Forwards/Backwards

a = Arduino()
pollSample1 = 10
pollSample2 = 3
pollSample3 = 1

def move_FR():
    a.analogWrite(rcLR,200)
    a.analogWrite(rcFB,0)
    
def move_FL():
    a.analogWrite(rcLR,0)
    a.analogWrite(rcFB,0)
    
def move_FS():
    a.analogWrite(rcLR,130)
    a.analogWrite(rcFB,0)
    
def move_R():
    a.analogWrite(rcLR,130)
    a.analogWrite(rcFB,70)
    
def move_IDLE():
    a.analogWrite(rcLR,130)
    a.analogWrite(rcFB,30)


def front_rightMic():
    x=0
    for i in range(0,pollSample1):
        sensor = a.analogRead(fR_MIC)
        x=x+sensor
    average=x/pollSample1
    return average

def front_leftMic():
    x=0
    for i in range(0,pollSample1):
        sensor = a.analogRead(fL_MIC)
        x=x+sensor
    average=x/pollSample1
    return average

def rear_rightMic():
    x=0
    for i in range(0,pollSample1):
        sensor = a.analogRead(rR_MIC)
        x=x+sensor
    average=x/pollSample1
    return average

def rear_leftMic():
    x=0
    for i in range(0,pollSample1):
        sensor = a.analogRead(rL_MIC)
        x=x+sensor
    average=x/pollSample1
    return average

def ultraSonicRear():
    x=0
    for i in range(0,pollSample3):
        a.digitalWrite(rearUStrigger , a.LOW)
        a.digitalWrite(rearUStrigger , a.HIGH)
        a.digitalWrite(rearUStrigger , a.LOW)
        pingTime = a.pulseIn(rearUSecho , a.HIGH);
        x=x+pingTime
    average=x/pollSample3
    return average

def ultraSonicFront():
    x=0
    for i in range(0,pollSample3):
        a.digitalWrite(frontUStrigger  , a.LOW)
        a.digitalWrite(frontUStrigger  , a.HIGH)
        a.digitalWrite(frontUStrigger  , a.LOW)
        pingTime = a.pulseIn(frontUSecho  , a.HIGH);
        x=x+pingTime
    average=x/pollSample3
    return average

def getCompassData():
    bus = smbus.SMBus(1)
    address = 0x1e
    
    def read_byte(adr):
        return bus.read_byte_data(address, adr)

    def read_word(adr):
        high = bus.read_byte_data(address, adr)
        low = bus.read_byte_data(address, adr+1)
        val = (high << 8) + low
        return val
    
    def read_word_2c(adr):
        val = read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
    
    def write_byte(adr, value):
        bus.write_byte_data(address, adr, value)
        
    write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
    write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
    write_byte(2, 0b00000000) # Continuous sampling
    
    scale = 0.92
    
    x=0
    for i in range(0,pollSample2):
        x_out = read_word_2c(3) * scale
        y_out = read_word_2c(7) * scale
        z_out = read_word_2c(5) * scale
        
        bearing  = math.atan2(y_out, x_out)
        if (bearing < 0):
            bearing += 2 * math.pi
        x = x+math.degrees(bearing)
    heading=x/ pollSample2
    return heading