
class Fleet:
    '''
    A class that represents all of a player's ships in battleship.
    '''

    def __init__(self):
        self.player_name = "Player Name"
        self.ship_list = []
        self.num_ships = 0

    def orderShips(self):
        '''
        
        '''
        sorted_ships = sorted(self.ship_list, key=Ship.asciiSymbol)
        self.ship_list = sorted_ships


class Ship:
    '''
    A class that represents one ship in battleship.
    '''

    def __init__(self):
        self.symbol = '?'
        self.size = 0

    def asciiSymbol(self):
        '''
        
        '''
        return ord(self.symbol)


class Board:
    '''
    A class that represents a board in battleship.
    '''

    def __init__(self):
        self.player_name = "Player Name"
        self.board_title = "Placement/Firing Board"
        self.see_board = []
        self.num_rows = 0
        self.num_cols = 0
        self.num_ships = 0
        self.num_destroyed = 0

    def drawBoard(self):
        '''

        '''
        title = self.player_name + "'s " + self.board_title
        print(title)
        for row in self.see_board:
            i = 0
            max = len(row) - 1
            for pos in row:
                print(pos, end = '')
                if i != max:
                    print(' ', end = '')
                else:
                    pass
                i += 1
            print('\n', end = '')
    
    def Place(self, ship, row_pos, col_pos, orientation):
        '''
        
        '''
        if orientation == "H":
            row = self.see_board[row_pos + 1]
            for i in range(0, ship.size):
                col = col_pos + i + 1
                row[col] = ship.symbol
            self.see_board[row_pos + 1] = row
        elif orientation == "V":
            for i in range(0, ship.size):
                row = self.see_board[row_pos + i + 1]
                row[col_pos + 1] = ship.symbol
                self.see_board[row_pos + i + 1] = row

    def Fire(self, opp, row_pos, col_pos):
        '''
        
        '''

        # check if hit a ship
        opp_row = opp.see_board[row_pos + 1]
        opp_location = opp_row[col_pos + 1]
        if opp_location == "*":
            hit_ship = False
            marker = 'O'
        elif opp_location != "*":
            hit_ship = True
            marker = 'X'
            symbol = opp_location

        # mark on opponent's placement board
        opp_row[col_pos + 1] = marker
        opp.see_board[row_pos + 1] = opp_row

        # mark on defense's firing board
        def_row = self.see_board[row_pos + 1]
        def_row[col_pos + 1] = marker
        self.see_board[row_pos + 1] = def_row

        # tell if missed or hit
        def_name = self.player_name
        opp_name = opp.player_name
        if hit_ship == True:
            print(def_name, ' hit ', opp_name, "'s ", symbol, '!', sep = '')
        elif hit_ship == False:
            print(def_name, 'missed.')
        
        # check if ship is destroyed now
        if hit_ship == True:
            ship_destroyed = True
            for row in opp.see_board:
                if symbol in row:
                    ship_destroyed = False
        else: 
            ship_destroyed = False
        
        # tell if ship is destroyed
        if ship_destroyed == True:
            print(def_name, ' destroyed ', opp_name, "'s ", symbol, '!', sep = '')
            opp.num_destroyed += 1


                

         
