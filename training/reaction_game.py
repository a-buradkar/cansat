#2LEDs and 2 switches - this demonstrates usage of IRQs

from machine import Pin
import utime
from urandom import uniform

led1 = Pin(12, Pin.OUT)
btn1 = Pin(14, Pin.IN)

led2 = Pin(11, Pin.OUT)
btn2 = Pin(13, Pin.IN)

pressed = False
def btn_handler(pin):
    global pressed
    
    if not pressed:
        if pin is btn1:
            print("P1 wins!")
            led2(0)
        else:
            print("P2 wins!")
            led1(0)

        print("Time:", utime.ticks_diff(utime.ticks_ms(), start) / 1000, "sec")
    
        pressed = True
       
led1(0)
led2(0)
utime.sleep(uniform(2, 5))
led1(1)
led2(1)

start = utime.ticks_ms()

btn1.irq(btn_handler, Pin.IRQ_RISING)
btn2.irq(btn_handler, Pin.IRQ_RISING)
