from machine import I2C
from bmp280 import BMP280

sda=machine.Pin(0)
scl=machine.Pin(1)
bus= I2C(0,sda=sda, scl=scl, freq=400000)
bmp = BMP280(bus)

pres = bmp.pressure
#international barometric formula, where 101600 is the exact current sea-level pressure (QNH)
altitude = 44330 * (1.0 - (pres/101600)**0.1903) # metres

print(bmp.temperature)
print(pres)
print(altitude)