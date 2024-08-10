# game.py

# packages
from battleship import Bosard

def runGame(placement_board_1: Board, placement_board_2: Board, firing_board_1: Board, firing_board_2: Board):
    '''
    
    '''

    game_over = False
    player_num = 1
    while game_over != True:

        turn(placement_board_1, placement_board_2, firing_board_1, firing_board_2, player_num)

        # check for winner
        if placement_board_1.num_destroyed == placement_board_1.num_ships:
            game_over = True
            winner = 2
        elif placement_board_2.num_destroyed == placement_board_2.num_ships:
            game_over = True
            winner = 1
        else:
            game_over = False

        # change player number
        if player_num == 1:
            player_num = 2
        elif player_num == 2:
            player_num = 1
        
    if winner == 1:
        firing_board_1.drawBoard()
        placement_board_1.drawBoard()
        winner_name = placement_board_1.player_name
    elif winner == 2:
        firing_board_2.drawBoard()
        placement_board_2.drawBoard()
        winner_name = placement_board_2.player_name

    print(winner_name, 'won!')

def turn(placement_board_1: Board, placement_board_2: Board, firing_board_1: Board, firing_board_2: Board, player_num: int):
    '''
    
    '''
    if player_num == 1:
        def_placement = placement_board_1
        def_firing = firing_board_1
        opp_placement = placement_board_2
    elif player_num == 2:
        def_placement = placement_board_2
        def_firing = firing_board_2
        opp_placement = placement_board_1
    
    name = def_placement.player_name

    def_firing.drawBoard()
    def_placement.drawBoard()

    fire_valid = False
    while fire_valid != True:
        print(name, ', enter the location you want to fire at in the form row col: ', sep = '', end = '')
        fire_input = input()
        fire_list = fire_input.split()
        # check if in correct form
        if len(fire_list) == 2:
            # check if all numbers
            if all(item.isdigit() for item in fire_list) == True:
                row_pos = int(fire_list[0])
                col_pos = int(fire_list[1])
                # check if row exists on board
                if row_pos < def_firing.num_rows:
                    # check if col exists on board
                    if col_pos < def_firing.num_cols:
                        # check if location has already been fired at:
                        row = def_firing.see_board[row_pos + 1]
                        location = row[col_pos + 1]
                        if location == '*':
                            fire_valid = True
    
    def_firing.Fire(opp_placement, row_pos, col_pos)


        
