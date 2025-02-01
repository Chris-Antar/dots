#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 1500, brightness=.5, auto_write=False)


for i in range(0, 300):
    pixels1[i] = (255, 0, 0)
    pixels1[599 - i] = (255, 0, 0)
    pixels1[600 + i] = (255, 0, 0)
    pixels1[1199 - i] = (255, 0, 0)
    pixels1[1200 + i] = (255, 0, 0)
    pixels1.show()
    time.sleep(.10)
    pixels1[i] = (0, 0, 0)
    pixels1[599 - i] = (0, 0, 0)
    pixels1[600 + i] = (0, 0, 0)
    pixels1[1199 - i] = (0, 0, 0)
    pixels1[1200 + i] = (0, 0, 0)


#pixels1[50]
#  = (255, 0, 0)


pixels1.fill((0, 0, 0))
pixels1.show()
#pixels1.show()





