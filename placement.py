# placement.py

from battleship import Board
from battleship import Fleet
from battleship import Ship

def enter_placement(board: Board, fleet: Fleet):
    '''
    
    '''
    board.drawBoard()
    player_name = board.player_name

    horiz_list = ['h', 'ho', 'hor', 'hori', 'horiz', 'horizo', 'horizon', 'horizont', 'horizonta', 'horizontal', 'horizontall', 'horizontally']
    vert_list = ['v', 've', 'ver', 'vert', 'verti', 'vertic', 'vertica', 'vertical', 'verticall', 'vertically']

    for ship in fleet.ship_list:
        all_valid = False
        while all_valid != True:
            # get orientation input
            orientation_valid = False
            while orientation_valid != True:
                print(player_name, ", enter the orientation of your ", ship.symbol, ", which is ", ship.size, " long: ", sep = "", end = "")
                orientation_input = str(input())
                orientation_input = orientation_input.lower()
                orientation_input = orientation_input.strip()
                if orientation_input in horiz_list:
                    orientation_valid = True
                    orientation = "H"
                elif orientation_input in vert_list:
                    orientation_valid = True
                    orientation = "V"
                else:
                    orientation_valid = False
            
            # get placement input
            placement_valid = False
            print('Enter the starting location for your ', ship.symbol, ', which is ', ship.size, ' long, in the form row col: ', sep = '', end = '')
            placement = str(input())
            placement_list = placement.split()
            # check if in correct form
            if len(placement_list) == 2:
                # check if all numbers
                if all(item.isdigit() for item in placement_list) == True:
                    row_pos = int(placement_list[0])
                    col_pos = int(placement_list[1])
                    # check if row exists on board
                    if row_pos < board.num_rows:
                        # check if col exists on board
                        if col_pos < board.num_cols:
                            # check if boat fits
                            if orientation == "H":
                                end_col_pos = col_pos + ship.size - 1
                                end_row_pos = row_pos
                            elif orientation == "V":
                                end_col_pos = col_pos
                                end_row_pos = row_pos + ship.size - 1
                            if end_col_pos < board.num_cols:
                                if end_row_pos < board.num_rows:
                                    # check if any other ships are there
                                    overlap_spaces = 0
                                    for i in range(0, ship.size):
                                        if orientation == "H":
                                            row = board.see_board[row_pos + 1]
                                            space = row[col_pos + i + 1]
                                            if space != "*":
                                                overlap_spaces += 1
                                        elif orientation == "V":
                                            row = board.see_board[row_pos + i + 1]
                                            space = row[col_pos + 1]
                                            if space != "*":
                                                overlap_spaces += 1
                                    if overlap_spaces == 0:
                                        placement_valid = True

            if placement_valid == False:
                all_valid = False
            elif placement_valid == True:
                all_valid = True

        board.Place(ship, row_pos, col_pos, orientation)
        board.drawBoard()
        board.num_ships += 1