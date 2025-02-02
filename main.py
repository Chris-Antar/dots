#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
from characters import ONE
from board_helpers import object_impose, object_accross

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 2700, brightness=.5, auto_write=False)

#object_impose(pixels1, ONE, 10, (255, 0, 0), 1)

object_accross(pixels1, ONE, (255, 0, 0), .30)


# for i in range(0, 300):
#     pixels1[i] = (255, 0, 0)
#     pixels1[599 - i] = (255, 0, 0)
#     pixels1[600 + i] = (255, 0, 0)
#     pixels1[1199 - i] = (255, 0, 0)
#     pixels1[1200 + i] = (255, 0, 0)
#     pixels1[1799 - i] = (255, 0, 0)
#     pixels1[1800 + i] = (255, 0, 0)
#     pixels1[2399 - i] = (255, 0, 0)
#     pixels1.show()
#     time.sleep(.10)
#     pixels1[i] = (0, 0, 0)
#     pixels1[599 - i] = (0, 0, 0)
#     pixels1[600 + i] = (0, 0, 0)
#     pixels1[1199 - i] = (0, 0, 0)
#     pixels1[1200 + i] = (0, 0, 0)
#     pixels1[1799 - i] = (0, 0, 0)
#     pixels1[1800 + i] = (0, 0, 0)
#     pixels1[2399 - i] = (0, 0, 0)


#pixels1[50]
#  = (255, 0, 0)


# pixels1.fill((0, 0, 0))
# pixels1.show()
#pixels1.show()





