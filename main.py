#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
from characters import ONE
from board_helpers import *

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 2700, brightness=.5, auto_write=False)

stocks_across(pixels1,[ONE, ONE, ONE], .30)
