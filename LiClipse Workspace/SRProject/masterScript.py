#!/usr/bin/python
from nanpy import Arduino
from nanpy import serial_manager
from time import sleep
import smbus
import time
import math
import sensorLibrary
a = Arduino()
sl = sensorLibrary

def noiseSource():
    frMIC = sl.front_rightMic()
    flMIC = sl.front_leftMic()
    rrMIC = sl.rear_rightMic()
    if (((frMIC+flMIC)/2) > rrMIC):
        #noise from front
        if (frMIC > flMIC):
            return "frontRight"
        else:
            return "frontLeft"
    else:
            return "rear"

def calculateHeading(): #I haven't finished this function because I don't feel like doing math right now
    nSource = noiseSource()
    currHeading = sl.getCompassData()
    if (nSource == "frontRight"):
        targetHeading = (currHeading )
        
    if (nSource == "frontLeft"):
        targetHeading = (currHeading )
        
    if (nSource == "rear"):
        targetHeading = (currHeading )

def moveTheDamnCar():
    nSource = noiseSource()
    if (nSource == "frontRight"):
        sl.move_IDLE()
        sl.move_FR()
        sleep(1)
        sl.move_FS()
        sleep(2)
        sl.move_IDLE()
        
    if (nSource == "frontLeft"):
        sl.move_IDLE()
        sl.move_FL()
        sleep(1)
        sl.move_FS()
        sleep(2)
        sl.move_IDLE()
        
    if (nSource == "rear"):
        sl.move_IDLE()
        sl.move_R()
        sleep(2)
        sl.move_IDLE()

def userTelometry():
    print("Heading = ",sl.getCompassData())
    nSource = noiseSource()
    if (nSource == "frontRight"):
        print("Moving forward Right")
    if (nSource == "frontLeft"):
        print("Moving Forward Left")
    if (nSource == "rear"):
        print("Moving Backwards")
    
while 1:
    userTelometry()
    moveTheDamnCar()