''' import from nanpy and time modules '''
from nanpy import Arduino
from nanpy import serial_manager
from time import sleep

''' create a connection to the Arduino '''
serial_manager.connect('/dev/ttyACM0')
