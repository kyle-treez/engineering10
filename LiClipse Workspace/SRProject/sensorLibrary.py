from nanpy import Arduino
from nanpy import serial_manager
from time import sleep
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
rcLR = 12 #Remote Control L&R port FORWARD
rcFB = 11 #Remote Control F&B port FRONT STREERING

a = Arduino()

def front_rightMic():
    x=0
    for i in range(0,10):
        sensor = a.analogRead(fR_MIC)
        x=x+sensor
    average=x/10
    return average

def front_leftMic():
    x=0
    for i in range(0,10):
        sensor = a.analogRead(fL_MIC)
        x=x+sensor
    average=x/10
    return average

def rear_rightMic():
    x=0
    for i in range(0,10):
        sensor = a.analogRead(rR_MIC)
        x=x+sensor
    average=x/10
    return average

def rear_leftMic():
    x=0
    for i in range(0,10):
        sensor = a.analogRead(rL_MIC)
        x=x+sensor
    average=x/10
    return average

def ultraSonicRear():
    x=0
    for i in range(0,10):
        a.digitalWrite(rearUStrigger , a.LOW)
        a.digitalWrite(rearUStrigger , a.HIGH)
        a.digitalWrite(rearUStrigger , a.LOW)
        pingTime = a.pulseIn(rearUSecho , a.HIGH);
        x=x+pingTime
    average=x/10
    return average

def ultraSonicFront():
    x=0
    for i in range(0,10):
        a.digitalWrite(frontUStrigger  , a.LOW)
        a.digitalWrite(frontUStrigger  , a.HIGH)
        a.digitalWrite(frontUStrigger  , a.LOW)
        pingTime = a.pulseIn(frontUSecho  , a.HIGH);
        x=x+pingTime
    average=x/10
    return average

def getCompassData():
    