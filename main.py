#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
from characters import matrix_map
from board_helpers import *

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 2700, brightness=.2, auto_write=False)

# stocks_across(pixels1,[ONE, ONE, ONE], .30)
time.sleep(5)
objects_impose(pixels1, [matrix_map["A"]], [6], (255, 0, 0))
objects_impose(pixels1, [matrix_map["B"]], [12], (255, 0, 0))
objects_impose(pixels1, [matrix_map["C"]], [18], (255, 0, 0))
objects_impose(pixels1, [matrix_map["D"]], [24], (255, 0, 0))
objects_impose(pixels1, [matrix_map["E"]], [30], (255, 0, 0))
objects_impose(pixels1, [matrix_map["F"]], [36], (255, 0, 0))
objects_impose(pixels1, [matrix_map["G"]], [42], (255, 0, 0))
objects_impose(pixels1, [matrix_map["H"]], [48], (255, 0, 0))
objects_impose(pixels1, [matrix_map["I"]], [54], (255, 0, 0))
objects_impose(pixels1, [matrix_map["J"]], [60], (255, 0, 0))
objects_impose(pixels1, [matrix_map["K"]], [66], (255, 0, 0))
objects_impose(pixels1, [matrix_map["L"]], [72], (255, 0, 0))
objects_impose(pixels1, [matrix_map["M"]], [78], (255, 0, 0))
objects_impose(pixels1, [matrix_map["N"]], [84], (255, 0, 0))
objects_impose(pixels1, [matrix_map["O"]], [90], (255, 0, 0))
objects_impose(pixels1, [matrix_map["P"]], [96], (255, 0, 0))
objects_impose(pixels1, [matrix_map["Q"]], [102], (255, 0, 0))
objects_impose(pixels1, [matrix_map["R"]], [108], (255, 0, 0))
objects_impose(pixels1, [matrix_map["S"]], [114], (255, 0, 0))
objects_impose(pixels1, [matrix_map["T"]], [120], (255, 0, 0))
objects_impose(pixels1, [matrix_map["U"]], [126], (255, 0, 0))
objects_impose(pixels1, [matrix_map["V"]], [132], (255, 0, 0))
objects_impose(pixels1, [matrix_map["W"]], [138], (255, 0, 0))
objects_impose(pixels1, [matrix_map["X"]], [144], (255, 0, 0))
objects_impose(pixels1, [matrix_map["Y"]], [150], (255, 0, 0))
objects_impose(pixels1, [matrix_map["Z"]], [156], (255, 0, 0))
objects_impose(pixels1, [matrix_map["0"]], [162], (255, 0, 0))
objects_impose(pixels1, [matrix_map["1"]], [168], (255, 0, 0))
objects_impose(pixels1, [matrix_map["2"]], [174], (255, 0, 0))
objects_impose(pixels1, [matrix_map["3"]], [180], (255, 0, 0))
objects_impose(pixels1, [matrix_map["4"]], [186], (255, 0, 0))
objects_impose(pixels1, [matrix_map["5"]], [192], (255, 0, 0))
objects_impose(pixels1, [matrix_map["6"]], [198], (255, 0, 0))
objects_impose(pixels1, [matrix_map["7"]], [204], (255, 0, 0))
objects_impose(pixels1, [matrix_map["8"]], [210], (255, 0, 0))
objects_impose(pixels1, [matrix_map["9"]], [216], (255, 0, 0))
