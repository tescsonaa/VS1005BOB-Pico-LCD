from ST7735 import TFT
from sysfont import sysfont
from machine import UART, SPI,Pin
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
vs_reset=Pin(22, Pin.OUT)   # VS1005 reset pin #  

# Define UART 
uart1=UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))


# HC4051 channel select #
def adc_mux(ch):
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
        adc_mux(ch)
        reading=analog_value.read_u16()
        y=x*10
        print("x=", x, "y=", y, "ADC", ch, ":", reading)
        string=("ADC=",ch, ":", (f'{reading:>5}'))
        print("string=", string)
        tft.text((0,y), str(string), TFT.WHITE, sysfont, 1, nowrap=False) 
        time.sleep(0.1)


async def uart_tx(x):
    swriter=asyncio.StreamWriter(uart1, {})
    string=x
    while True:
        await swriter.awrite(string)
        print("Send:", string)
        await asyncio.sleep(1)

async def uart_rx():
    sreader=asyncio.StreamReader(uart1)
    while True:
        res=await sreader.readline()
        print('Recieved', res)



def main_run():
    # TFT init #
    print("Start programme")
    tft.initr()
    tft.rgb(True)
    tft.rotation(1)
    tft.fill(TFT.BLACK);   # Turn off LCD display #
    
    print("Start reset")
    led.value(1)    
    vs_reset.value(1)   # Start VS1005 reset  # 
    time.sleep(2)   
    led.value(0)   
    vs_reset.value(0)    
    time.sleep(2)
    led.value(1) 
    vs_reset.value(1)   # End VS1005 reset # 
    time.sleep(2)
    

    # VS1005 load driver # 
    string="driver + FTOEQU" 
    print("s1:", string) 
    uart1.write(string)   

    adc_scan() 
    









# Test code #
def main():
    loop=asyncio.get_event_loop()
    print("start loop")
    loop.create_task(uart_rx())
    loop.create_task(main_run())
    loop.run_forever()

main()



    
    
