#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode (GPIO.BOARD)
GPIO.setup (5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
     trigger = GPIO.input(5)
     if trigger == False:
          subprocess.call("espeak \"Shutting down ... Goodbye\" 2>/dev/null", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          subprocess.call("init 0", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     time.sleep(.1)


