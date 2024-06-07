from machine import Pin, SPI
import st7789

TFA = 0
BFA = 0

def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(1, baudrate=20000000, sck=Pin(10), mosi=Pin(11)),
        128,
        160,
        reset=Pin(17, Pin.OUT),
        cs=Pin(18, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(15, Pin.OUT),
        color_order=st7789.RGB,
        inversion=False,
        rotation=rotation,
        options=options,
        buffer_size=buffer_size)