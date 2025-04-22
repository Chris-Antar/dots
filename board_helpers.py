import time

BOARD_WIDTH = 300
BOARD_HEIGHT = 9

def objects_impose(board, board_objects, start_cols, blank=False):
    """
    Imposes a list of objects on the board at specified start columns
    """
    cur_obj_col = 0
    # if start_cols[cur_col] > BOARD_WIDTH dont do anything
    for object in board_objects:
        if blank:
            color = (0, 0, 0)
        else:
            color = object.color
        row = len(object.shape)
        for i in object.shape:
            col = 0
            for j in reversed(i):
                if  start_cols[cur_obj_col] - col < 0:
                    break
                if j == 0:
                    col += 1
                    continue
                else:
                    if row % 2 == 0:
                        board[(row * 300) - 1 - start_cols[cur_obj_col] + col] = color
                    else:
                        board[((row - 1) * 300) + start_cols[cur_obj_col]  - col] = color
                    
                col += 1
            row -= 1
        cur_obj_col += 1
    #remove this, it slows it down, only show after all updates are made
    board.show()



def stocks_across(board, objects, duration: float):
    """
    Sequentially moves a list of stock objects across the board
    """
    ticker_index = 1 
    positions = [0]
    total_objects_length = len(objects[0].shape[0])
    #Change board width to 300 + len(tickers) * len(ticker) for ticker in tickers
    for i in range(BOARD_WIDTH):
        if ticker_index < len(objects):
            if i > total_objects_length:
                total_objects_length += (len(objects[ticker_index].shape[0])) + 1
                ticker_index += 1
                positions.append(0)
        # add objects and start positions
        objects_impose(board, objects[:ticker_index], positions)
        time.sleep(duration)
        # test board_fill(0,0,0) performance opposed to this
        objects_impose(board, objects[:ticker_index], positions, True)

        #increment position
        positions = [x + 1 for x in positions]




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

