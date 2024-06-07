from ST7735 import TFT
from sysfont import sysfont
from machine import UART, SPI,Pin
from uart_async import uart_rx, uart_tx
import uasyncio as asyncio
import asyncio
import time

# Define SPI bus for LCD display 128*160 # 
spi=SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=None)
tft=TFT(spi,16,17,18)      # DC, Reset, CS

# Define ADC and HC4051 control pins #
analog_value = machine.ADC(26)
Sel0=Pin(0, Pin.OUT)
Sel1=Pin(1, Pin.OUT)
Sel2=Pin(2, Pin.OUT)

# Define GPIO # 
led=Pin(25, Pin.OUT)


# HC4051 channel select #
def adc_mux():
    if ch==0: Sel0(0), Sel1(0), Sel2(0)
    elif ch==1: Sel0(1), Sel1(0), Sel2(0)
    elif ch==2: Sel0(0), Sel1(1), Sel2(0)
    elif ch==3: Sel0(1), Sel1(1), Sel2(0)
    elif ch==4: Sel0(0), Sel1(0), Sel2(1)
    elif ch==5: Sel0(1), Sel1(0), Sel2(1)
    elif ch==6: Sel0(0), Sel1(1), Sel2(1)
    else: Sel0(1), Sel1(1), Sel2(1)


def adc_scan():
    y=0
    for x in range(8):
        ch=x
        adc_mux()
        reading=analog_value.read_u16()
        y=x*10
        print("x=", x, "y=", y, "ADC", ch, ":", reading)
        string=("ADC=",ch, ":", (f'{reading:>5}'))
        print("string=", string)
        tft.text((0,y), str(string), TFT.WHITE, sysfont, 1, nowrap=False) 
        time.sleep(0.1)





