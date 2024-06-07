from machine import Pin, UART, ADC
import array
import time

import st7789
import tft_config
import romanp as font2
import vga1_8x8 as font1
import vga2_bold_16x32 as font3

tft = tft_config.config(1)

from lcd_display import lcd_frame 


# Define UART #
uart1=UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))

# Define GPIO # 
led=Pin(25, Pin.OUT)
# Define ADC and HC4051 control pins #
analog_value=ADC(26)
Sel0=Pin(0, Pin.OUT)
Sel1=Pin(1, Pin.OUT)
Sel2=Pin(2, Pin.OUT)

# Define GPIO # 
led=Pin(25, Pin.OUT)

y=0
#print(y)
int_array=array.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
old_array=array.array('i', [1, 2, 3, 4, 5, 6, 7, 8])



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


def adc_read():
    
    print("Start adc_read()")

    for x in range(8):
        ch=x
        adc_mux(ch)
        
        print("saved_int_array ch=", ch, "ADC=", old_array[ch])
        tft.hline((30+ch*15+10), 35+old_array[ch], 5, st7789.BLACK)	# clean old bar #
        tft.hline((30+ch*15+16), 35+old_array[ch], 4, st7789.BLACK)	# clean old bar #
        
        reading=analog_value.read_u16()
        int_array[ch]=reading//820	# save current ADC value
        old_array[ch]=reading//820
        print("int_array ch=", ch, "ADC=", int_array[ch])
        print("old_array ch=", ch, "ADC=", old_array[ch])
        tft.hline((30+ch*15+10), 35+int_array[ch], 5, st7789.WHITE)	# print new bar # 
        tft.hline((30+ch*15+16), 35+int_array[ch], 4, st7789.WHITE)	# print new bar # 
        
            
        time.sleep(0.03)
            
'''
            remove_bar=int_array[x-1]
            tft.fill_rect(((x-1)*15-5), 35, 82, 5, st7789.BLACK)
            
'''

''' Display ADC value for testing
        string=("ADC=",ch,(f'{reading:>5}'))
        tft.text(font1, str(string), 0, y, st7789.WHITE, st7789.BLACK)
        tft.fill_rect((x*15-5), 35, 82, 5, st7789.BLACK)
        tft.fill_rect((x+1)*15-5, 35+(reading//820), 10, 5, st7789.RED)
''' 








# Test code 
def adc_main():
    print("Start programme")
    tft.init()
    tft.fill(st7789.BLACK)
    lcd_frame()
    ch=0
    while True:
        adc_read()


adc_main() 

