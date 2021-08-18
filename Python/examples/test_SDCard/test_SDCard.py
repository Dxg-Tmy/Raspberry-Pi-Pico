from machine import Pin, SoftSPI
import time
import pack.sdcard.sdcard as im_sdcard
import os #what is different between os and uos

# Initialize the SD card
''' 
SDCard_Pin SDIO/SPI  #_# This PINS are fit <eetree.cn>'s pico board;if u not fit,change PINS.
1 DAT2/NC   = Pin(21)
2 DAT3/CS   = Pin(22)
3 CMD /MOSI = Pin(18)
4 VDD /VDD  = VCC[3.3v]
5 CLK /SCLK = Pin(17)
6 VSS /VSS  = GND
7 DAT0/MISO = Pin(19)
8 DAT1/NC   = Pin(20)
'''
sd_spi= SoftSPI(sck=Pin(17), mosi=Pin(18), miso=Pin(19))
sd= im_sdcard.SDCard(spi=sd_spi,cs=machine.Pin(22))
sd.init_card()

# Create a instance of MicroPython Unix-like Virtual file_handle System (VFS),
# Mount file_handlesystem
strSDCardName = '/sd'
vfs = os.VfsFat(sd)
os.mount(vfs, strSDCardName)
# Debug print SD card directory and file_handles
print('---')
print(os.listdir(strSDCardName))

print('---')
for file_handlename in os.listdir(strSDCardName):
    print(strSDCardName+'/'+file_handlename)


print('\r\n---write/read way1')
# Create / Open a file_handle in write mode.
# Write mode creates a new file_handle.
# If  already file_handle exists. Then, it overwrites the file_handle.
file_handle = open(strSDCardName+"/sample.txt","w+a")
# Write sample text
for i in range(20):
    file_handle.write("Sample text = %s\r\n" % i)
# Close the file_handle
file_handle.close()


# Again, open the file_handle in "append mode" for appending a line
file_handle = open(strSDCardName+"/sample.txt","a")
file_handle.write("Appended Sample Text at the END \n")
file_handle.close()

# Open the file_handle in "read mode". 
# Read the file_handle and print the text on debug port.
file_handle = open(strSDCardName+"/sample.txt", "r")
if file_handle != 0:
    print("Reading from SD card")
    read_data = file_handle.read()
    print (read_data)
file_handle.close()

# Initialize timer_one. Used for toggling the on board LED
timer_one = machine.Timer()
# Timer one initialization for on board blinking LED at 200mS interval
##timer_one.init(freq=5, mode=machine.Timer.PERIODIC, callback=BlinkLED)

print('\r\n---write/read way2')
# Create a file_handle and write something to it
with open(strSDCardName+"/test01.txt", "w") as file_handle:
    file_handle.write("Hello, SD World!\r\n")
    file_handle.write("This is a test\r\n")

# Open the file_handle we just created and read from it
with open(strSDCardName+"/test01.txt", "r") as file_handle:
    data = file_handle.read()
    print(data)
    
#End
