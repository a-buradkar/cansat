#setup: an RGB LED with rgb terminals connected to pins 10, 11, 12 respectively with a resistor in between,
# and the common cathode connected to ground. Use a 330 Ohm resistor for red and 1k Ohm for blue and green
#demonstrates PWM usage and RGB LED usage and rainbows

from machine import Pin, ADC, PWM
from utime import sleep

import math

freq = 1000 # number of times the duty cycle of a PWM updates/s

r = PWM(Pin(10), freq=freq)
g = PWM(Pin(11), freq=freq)
b = PWM(Pin(12), freq=freq)


T = 2.5 # time period of a complete cycle

i = 0 # starting value of i, doesn't really matter 
di = 2*math.pi / freq / T 

u16_factor = 65535/2
phase = 2 * math.pi / 3

while True:
    r_v = int((math.sin(i) + 1)           * u16_factor)
    g_v = int((math.sin(i + phase)   + 1) * u16_factor)
    b_v = int((math.sin(i + 2*phase) + 1) * u16_factor)
    
    
    r.duty_u16(r_v)
    g.duty_u16(g_v)
    b.duty_u16(b_v)
    
    i += di
    sleep(1/freq)