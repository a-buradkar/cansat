import digitalio
import board
import busio
import adafruit_bmp280
import adafruit_rfm9x

from time import sleep

def send(msg):
    return rfm.send(msg)
    
def receive(t=1.0):
    return rfm.receive(timeout=t)
    
def rssi():
    return rfm.rssi

spi = busio.SPI(clock = board.GP2, MOSI = board.GP3, MISO = board.GP4)
cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

rfm = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

print("RFM96 radio ready")