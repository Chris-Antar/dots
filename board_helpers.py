import time





def object_impose(board, board_object, start_col, color):
    row = 9
    for i in board_object:
        col = 0
        for j in i:
            if j == 0:
                col += 1
                continue
            else:
                if row % 2 == 0:
                    board[(row * 300) - 1 - start_col - col] = color
                else:
                    board[((row - 1) * 300) + start_col + col] = color
                
            col += 1
        row -= 1
    board.show()


def object_accross(board, board_object, color, duration):
    for i in range(0, 300 - len(board_object[0])):
        object_impose(board, board_object, i, color)
        time.sleep(duration)
        object_impose(board, board_object, i, (0, 0, 0))



