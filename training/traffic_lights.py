# 3 LEDs connected to pins 10,11,12 and a buzzer on pin 0. Also 1 switch on pin 14, don't forget resistors on LEDs
from machine import Pin
from random import randrange

import utime


def set_values(r, y, g, w=0):
    global red, yellow, green
    red(r)
    yellow(y)
    green(g)
    
    utime.sleep(w)
    

btn = Pin(14, Pin.IN, Pin.PULL_DOWN)

red = Pin(12, Pin.OUT)
yellow = Pin(11, Pin.OUT)
green = Pin(10, Pin.OUT)
buzzer = Pin(0, Pin.OUT)
    
set_values(0, 0, 1)
buzzer(0)

while True:
    if btn() == 1:
        # green
        set_values(0, 1, 0, 1) # yellow
        set_values(1, 0, 0) # red
        
        for _ in range(10):
            buzzer.toggle()
            utime.sleep(0.2)
            
        set_values(1, 1, 0, 1) # red + yellow
        set_values(0, 0, 1, 1) # green
 