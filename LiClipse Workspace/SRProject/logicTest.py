#!/usr/bin/python
import sensorLibrary
from nanpy import Arduino
from nanpy import serial_manager
from time import sleep
import smbus
import time
import math
from random import randint
s = sensorLibrary
a = Arduino()

while 1:
        ran1=(randint(0,15))
        ran2=(randint(0,15))
        sleep(randint(2,8))
        if randint(0,1) == 1:
            a.analogWrite(6,ran1)
        else:
            a.analogWrite(5,ran1)

        if randint(0,1) == 1:
            a.analogWrite(7,ran2)
        else:
            a.analogWrite(5,ran2)

        print("r1 p6 =", ran1)
        print("r2 p7 =", ran2)
