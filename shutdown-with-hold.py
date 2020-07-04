#!/usr/bin/env python3

from gpiozero import Button
from signal import pause
import os, sys

offGPIO = 21
holdTime = 2

# the function called to shut down the RPI
def shutdown():
    os.system("sudo poweroff")

btn = Button(offGPIO, hold_time=holdTime)
btn.when_held = shutdown
pause()    # handle the button presses in the background
