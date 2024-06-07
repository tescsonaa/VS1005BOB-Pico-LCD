from machine import Pin
import time

import st7789
import tft_config
import romanp as font2
import vga1_8x8 as font1
tft=tft_config.config(1)


# Define GPIO # 
led=Pin(25, Pin.OUT)


# Test code 
def lcd_frame():
    # TFT init #
    print("Start programme")
    tft.init()
    tft.fill(st7789.BLACK)

#    tft.text(0, 0, "Test", TFT.WHITE, sysfont, 1, nowrap=False)
    tft.text(font1, "7-Band Equalizer", 17, 0, st7789.WHITE, st7789.BLACK)
    tft.text(font1, " Bass = 80 Hz", 25, 14, st7789.WHITE, st7789.BLACK) 

    tft.vline(45, 35, 82, st7789.BLUE)	# EQ 0 vline(x, y, long, colour)
    tft.vline(60, 35, 82, st7789.BLUE)	# EQ 1
    tft.vline(75, 35, 82, st7789.BLUE)	# EQ 2
    tft.vline(90, 35, 82, st7789.BLUE)	# EQ 3
    tft.vline(105, 35, 82, st7789.BLUE)	# EQ 4
    tft.vline(120, 35, 82, st7789.BLUE)	# EQ 5
    tft.vline(135, 35, 82, st7789.BLUE)	# EQ 6
    tft.vline(150, 35, 82, st7789.BLUE)	# EQ 7

    tft.text(font1, "100", 5, 35, st7789.WHITE, st7789.BLACK)
    tft.text(font1, "0", 5, 70, st7789.WHITE, st7789.BLACK)
    tft.text(font1, "-100", 5, 105, st7789.WHITE, st7789.BLACK)




    tft.pixel(45, 75, st7789.RED)
    tft.pixel(60, 75, st7789.RED)
    tft.pixel(75, 75, st7789.RED)
    tft.pixel(90, 75, st7789.RED)
    tft.pixel(105, 75, st7789.RED)
    tft.pixel(120, 75, st7789.RED)
    tft.pixel(135, 75, st7789.RED)
    tft.pixel(150, 75, st7789.RED)
 
 
 
'''
# Test code #
lcd_frame() 
''' 
