import uasyncio as asyncio
import time
from machine import UART, SPI,Pin


uart1=UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))

# Define GPIO # 
led=Pin(25, Pin.OUT)
vs_reset=Pin(22, Pin.OUT)   # VS1005 reset pin #  


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







# Test code #
def test_code():
    string="test test test"
    print(string)

    loop=asyncio.get_event_loop()
    loop.create_task(uart_tx(string))
    loop.create_task(uart_rx())
    loop.run_forever()

# test_code()

    
    
    
    