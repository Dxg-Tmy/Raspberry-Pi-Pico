from machine import Pin
import time

led = Pin(25,Pin.OUT)

while True:
    led.toggle() #LED翻转
    time.sleep(.5)
