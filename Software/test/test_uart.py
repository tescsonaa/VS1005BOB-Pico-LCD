from machine import UART, Pin
uart1 = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))

buffer = b""
buffer_ready = False

while True:   
    if uart1.any():
        c = uart1.read(1)
        if c == b'\n':
            buffer_ready = True
        else:    
            buffer += c
    if buffer_ready:
        print(buffer)
        buffer = b""
        buffer_ready = False
