# one pot with signal pin 26, and LED pin 10. Dimmable light program to show ADC and PWM
from machine import Pin, ADC, PWM
from utime import sleep

led = PWM(Pin(10), freq=1000)
pot = ADC(26)

while True:
    led.duty_u16(pot.read_u16())
    