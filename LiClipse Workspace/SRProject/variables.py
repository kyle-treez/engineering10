from nanpy import Arduino
from nanpy import serial_manager
from time import sleep
a = Arduino()

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
compData = 46; # Compass Data
compClock = 47 # Compass Clock

#Remote controls use Pulse Wave Modulation digital outputs
rcLR = 12 #Remote Control L&R port FORWARD
rcFB = 11 #Remote Control F&B port FRONT STREERING

