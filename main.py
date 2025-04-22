#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
from characters import matrix_map, combine_2d_arrays
from board_helpers import *
from board_object import BoardObject
from stocks import get_stock_data

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 2700, brightness=.5, auto_write=False)

stocks = get_stock_data()
stock_objects = []
print(stocks)

for k, v in stocks.items():
    if v > 0:
        color = GREEN
    else:
        color = RED

    # Create a BoardObject for each stock
    chars = list(k)
    word = matrix_map[chars[0]]

    for char in chars[1:]:
        word = combine_2d_arrays([word, matrix_map[char]])

    if v > 0:
        word = combine_2d_arrays([word, matrix_map["up"]])
        pct = str(v) 
        for char in pct:
            word = combine_2d_arrays([word, matrix_map[char]])
    else:
        word = combine_2d_arrays([word, matrix_map["down"]])
        pct = str(v) 
        for char in pct:
            if char == "-":
                continue
            word = combine_2d_arrays([word, matrix_map[char]])

    stock_objects.append(BoardObject(word, color))

stocks_across(pixels1, stock_objects, .30)

