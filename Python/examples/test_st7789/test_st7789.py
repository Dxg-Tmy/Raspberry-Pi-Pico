import pack.st7789.st7789py as im_st7789
from pack.fonts import vga2_8x8 as im_font_8x8
from pack.fonts import vga1_16x32 as im_font_8x8_16x32
import time
#LCD_init
LCD_width = 240 #depends on the actual device
LCD_height = 240#depends on the actual device
LCD_CENTER_Y = int(LCD_width/2)
LCD_CENTER_X = int(LCD_height/2)
spi0 = machine.SPI(0, baudrate=40000000, polarity=1, phase=0, sck=machine.Pin(2), mosi=machine.Pin(3))
LCD_display = im_st7789.ST7789(
    spi0,
    LCD_width,
    LCD_width,             
    reset=machine.Pin(0, machine.Pin.OUT),
    dc=machine.Pin(1, machine.Pin.OUT),
    xstart=0,
    ystart=0,
    rotation=0)
#RotarySw init
RotarySw_DownUp = machine.Pin(6,machine.Pin.IN)
RotarySw_TurnLeft=machine.Pin(4,machine.Pin.IN)
RotarySw_TurnRight=machine.Pin(5,machine.Pin.IN)
##LCD_display.fill(st7789.color565(0, 255, 120))
LCD_display.fill(im_st7789.BLACK)
LCD_display.text(im_font_8x8_16x32, "Hello!", 10, 10)
time.sleep(.01)
LCD_display.text(im_font_8x8_16x32, "RPi Pico", 10, 40)
time.sleep(.01)
LCD_display.text(im_font_8x8_16x32, "Piday eetree ", 10, 70)
time.sleep(.01)
LCD_display.text(im_font_8x81, "ST7789 SPI 240*240 IPS", 10, 100)
time.sleep(.01)
LCD_display.text(im_font_8x81, "eetree.cn", 10, 110)
time.sleep(.01)
LCD_display.text(im_font_8x81, "Piday, let's have fun!", 10, 120)
time.sleep(.01)