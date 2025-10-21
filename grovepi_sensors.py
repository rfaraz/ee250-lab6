import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    # threshold = grovepi.analogRead(potentiometer)
    threshold = int((grovepi.analogRead(potentiometer) / 1024 ) * 518)
    
    # TODO: format LCD text according to threshhold
    if distance < threshold:
        top_line = f"{threshold:3d}cm OBJ PRES"
    else:
        top_line = f"{threshold:3d}cm"
    bottom_line = f"{distance:3d}cm"
    setText_norefresh(top_line + "\n" + bottom_line)
    
  except IOError:
    print("Error")
