import digitalio
import board
import busio
import storage

import adafruit_bmp280
import radio
from time import sleep

CANSAT = True
write_en = not storage.getmount("/").readonly
print("internal file writing enabled:", write_en)
# led = digitalio.DigitalInOut(board.GP25)
# led.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
n=0

while CANSAT:
    msg=f"{n},{bmp.pressure},{bmp.temperature}"
    with open("/results.txt", "a") as file:
        file.write(msg)
    radio.send(msg)
    
#     print(n, "sent")
    sleep(1)
    n+=1
    
while not CANSAT:
    msg = radio.receive()
    if msg is not None:
        print("msg:", str(msg,'ascii'))
        print("RSSI:", radio.rssi())
        print()

