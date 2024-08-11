



def create_board(rows, columns):
    '''
            Parameters:
           rows: number of rows
           columns: number of columns

            Returns:
                board: list of lists

    '''
    """Create and return a game board initialized with empty spaces."""
    return [["*" for _ in range(columns)] for _ in range(rows)]

def print_board(board):
    """Print the game board to the console with row and column indices."""
    '''
            Parameters:
            board: list of lists
            columns: number of columns

            Returns:
             prints the game board to the console with row and column indices.
    '''
    columns = len(board[0])
    # Print column indices
    print("  " + " ".join(str(i) for i in range(columns)))
    # Print the board with row indices
    for idx, row in enumerate(reversed(board)):
        print(f"{len(board) - 1 - idx} " + " ".join(row))

def get_valid_input(prompt):
    """Prompt the user for a positive integer input."""
    '''
            Parameters:
            promty: input a positive integer

            Returns:
             a positive integer or an empty string if user inputs invalid.
    '''
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            continue

def get_valid_move(board, columns):
    """Prompt the user for a valid move (column number)."""
    '''
            Parameters:
            asks the user to enter a valid move in a column.

            Returns:
             puts the move in the board.
    '''
    while True:
        try:
            column = int(input("Enter the column you want to play in: "))
            if 0 <= column < columns and board[-1][column] == "*":
                return column
        except ValueError:
            continue

def place_piece(board, column, player):
    """Place the player's piece in the specified column."""
    '''
            Parameters:
            column: column number
            row: row number

            Returns:
             puts the piece in the specified column.
    '''
    for row in range(len(board)):
        if board[row][column] == "*":
            board[row][column] = player
            return

def switch_player(current_player):
    """Switch the current player and return the next player."""
    '''
            Parameters:
            current_player: player number

            Returns:
             switch the current player and return the next player.
           
    '''
    return "O" if current_player == "X" else "X"

def check_winner(board, player, n_to_win):
    """Check if the current player has won the game."""
    '''
            Parameters:
            board: list of lists
            player: player number
            n_to_win: number of winning players
            

            Returns:
             checks if the current player has won the game or not.
    '''
    rows = len(board)
    columns = len(board[0])
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for row in range(rows):
        for col in range(columns):
            if board[row][col] == player:
                for dr, dc in directions:
                    if check_line(board, player, row, col, dr, dc, n_to_win):
                        return True
    return False

def check_line(board, player, row, col, dr, dc, n):
    """Check a line of pieces in a specific direction for a win."""
    '''
            Parameters:
            board: list of lists
            player: player number
            row: row number
            dr = direction number
            dc = direction number
            n: number of pieces to check
            

            Returns:
             checks if the pieces are in a specific direction to win.
    '''
    for i in range(n):
        r = row + dr * i
        c = col + dc * i
        if not (0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == player):
            return False
    return True

def is_board_full(board):
    """Check if the board is full."""
    '''
            Parameters:
            board: list of lists

            Returns:
             checks if the board is full or not.
    '''
    for row in board:
        if "*" in row:
            return False
    return True

def main():
    """Main function to run the Connect-N game."""
    '''
            Parameters:
            rows: number of rows
            columns: number of columns
            n_to_win: number of winning players
            board: list of lists
            player: player number
            place_piece: function to place the piece in the specified column
            check_piece: function to check if the piece is in the specified column
            switch_player: function to switch the current player and return the next player.
            check_winner: function to check if the current player has won the game or not.
            check_line: function to check if the current player has won the game or not.
            is_board_full: function to check if the board is full or not.
            

            Returns:
             all the values of the game board after the game is completed.
        '''
    rows = get_valid_input("Enter the number of rows: ")
    columns = get_valid_input("Enter the number of columns: ")
    n_to_win = get_valid_input("Enter the number of pieces in a row to win: ")

    board = create_board(rows, columns)
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        column = get_valid_move(board, columns)
        place_piece(board, column, current_player)

        if check_winner(board, current_player, n_to_win):
            print_board(board)
            if current_player == "X":
                print("Player 1 won!")
            else:
                print("Player 2 won!")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("Tie Game")
            game_over = True
        else:
            current_player = switch_player(current_player)

if __name__ == "__main__":
    main()
