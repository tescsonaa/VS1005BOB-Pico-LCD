from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

sw_pin = Pin(24, machine.Pin.IN, machine.Pin.PULL_UP)

while True: 
    led.value(1)
    temp=sw_pin.value()
    print(temp)
    sleep(1)
