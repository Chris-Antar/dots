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
                # Object behind start
                if  start_cols[cur_obj_col] - col < 0:
                    break
                # Object in after finish
                if start_cols[cur_obj_col] - col >= BOARD_WIDTH:
                    col += 1
                    continue
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
    i = 0
    while True:
        if ticker_index < len(objects):
            if i > total_objects_length:
                total_objects_length += (len(objects[ticker_index].shape[0])) + 1
                ticker_index += 1
                positions.append(0)
        # add objects and start positions
        objects_impose(board, objects[:ticker_index], positions)
        time.sleep(duration)
        # test board_fill(0,0,0) performance opposed to this
        board.fill((0, 0, 0))
        #increment position
        positions = [x + 1 for x in positions]
        i += 1
        #Chagne to > bnoard width if going away too early
        if positions[0] - len(objects[0].shape[0]) >= BOARD_WIDTH:    
            positions.pop(0)
            object = objects.pop(0)
            objects.append(object)  
            
            ticker_index -= 1
            i -= len(objects[ticker_index - 1].shape[0])
            total_objects_length -= len(objects[ticker_index - 1].shape[0])
