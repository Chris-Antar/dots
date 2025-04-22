#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
from characters import matrix_map, combine_2d_arrays
from board_helpers import *
from board_object import BoardObject

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 2700, brightness=.5, auto_write=False)


temp = combine_2d_arrays([matrix_map["up"], matrix_map["down"]])
objects_impose(pixels1, [BoardObject(temp, RED)], [50], blank=False)
# stocks_across(pixels1,[red_nine, red_8, red_nine], .30)

