from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

def blink(secs):
    while True:
        led.on()
        print ("on")
        sleep(secs)
        led.off()
        print ("off")
        sleep(secs)
