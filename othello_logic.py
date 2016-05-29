#Project 5 Kevin Yin 29211757
#Othello Game Logic

        
def make_move(game: 'Gamestate', Column: int, Row: int, apply: str)-> str:
    '''Takes in a Gamestate object and a move set. Returns 'VALID' when a move is allowed and
    'INVALID' when it is illegal. If the apply value is 'YES', then the move will be applied to the board.
    Values taken into this function are based on the python 0+ numbering scale. '''

    RESULT= 'INVALID'

    if Column+1 > game.columns or Column < 0 or Row+1 > game.rows or Row < 0:
        return 'INVALID'
    if game.board[Column][Row] == 'B' or game.board[Column][Row] == 'W' or game.board_status() == 'FULL':
        return 'INVALID'
    
    row= Row
    #check north
    while True: 
        row = row - 1
        if row < 0:
            break
        else:
            if game.board[Column][row] == 0 or game.board[Column][Row-1] == game.turn:
                break
            elif game.board[Column][row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    start= row
                    for space in range(start ,Row ):
                        game.board[Column][space] = game.turn
                    break
                else:
                    break

    #check east
    col= Column
    while True:
        col = col + 1
        if col + 1 > game.columns:
            break
        else:
            if game.board[col][Row] == 0 or game.board[Column+1][Row] == game.turn:
                break
            elif game.board[col][Row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    end= col
                    for col in range(Column+1, end ):
                        game.board[col][Row] = game.turn
                    break
                else:
                    break

    #check south
    row= Row
    while True:
        row= row + 1
        if row + 1 > game.rows:
            break
        else:
            if game.board[Column][row] == 0 or game.board[Column][Row+1] == game.turn:
                break
            elif game.board[Column][row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    end= row
                    for row in range(Row+1, end ):
                        game.board[Column][row] = game.turn
                    break
                else:
                    break
    

    #check west
    col= Column
    while True:
        col = col - 1
        if col < 0:
            break
        else:
            if game.board[col][Row] == 0 or game.board[Column-1][Row] == game.turn:
                break
            elif game.board[col][Row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    start = col
                    for col in range(start , Column ):
                        game.board[col][Row] = game.turn
                    break
                else:
                    break


    #check northeast
    col= Column
    row= Row
    
    while True:
        col += 1
        row -= 1
        if col + 1 > game.columns or row < 0:
            break
        else:
            if game.board[col][row] == 0 or game.board[Column+1][Row-1] == game.turn:
                break
            elif game.board[col][row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    end= col
                    row= Row
                    for col in range(Column+1, end ):
                        row -= 1
                        game.board[col][row] = game.turn
                    break
                else:
                    break

    #check southeast
    col= Column
    row= Row
    while True:
        col += 1
        row += 1
        if col + 1 > game.columns or row+1 > game.rows:
            break
        else:
            if game.board[col][row] == 0 or game.board[Column+1][Row+1] == game.turn:
                break
            elif game.board[col][row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    end= col
                    row= Row
                    for col in range(Column+1, end ):
                        row += 1
                        game.board[col][row] = game.turn
                    break
                else:
                    break

    #check northwest
    col= Column
    row= Row
    while True:
        col -= 1
        row -= 1
        if col < 0 or row < 0:
            break
        else:
            if game.board[col][row] == 0 or game.board[Column-1][Row-1] == game.turn:
                break
            elif game.board[col][row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    start= col
                    for col in range(start, Column):
                        game.board[col][row] = game.turn
                        row += 1
                    break
                else:
                    break

    #check southwest
    col= Column
    row= Row
    while True:
        col -= 1
        row += 1
        if col < 0 or row + 1 > game.rows:
            break
        else:
            if game.board[col][row] == 0 or game.board[Column-1][Row+1] == game.turn:
                break
            elif game.board[col][row] == game.turn:
                RESULT= 'VALID'
                if apply == 'YES':
                    start= col
                    for col in range(start, Column):
                        game.board[col][row] = game.turn
                        row -= 1
                    break
                else:
                    break

    if apply == 'YES' and RESULT == 'VALID':
        game.board[Column][Row] = game.turn
        if game.turn== 'B':
            game.turn= 'W'
        else:
            game.turn= 'B'

    return RESULT

class Gamestate:

    def __init__(self, rows: int, columns: int, top_left: str, first: str, game_type):
        board= []
        for col in range(int(columns)):
            board.append([])
            for row in range(int(rows)):
                board[-1].append(0)
        middle_top_col= int(columns/2 - 1)
        middle_top_row= int(rows/2 - 1)
        
        if top_left== 'B':
            top_right= 'W'
        else:
            top_right= 'B'
            
        board[middle_top_col][middle_top_row] = top_left
        board[middle_top_col + 1][middle_top_row]= top_right
        board[middle_top_col][middle_top_row + 1]= top_right
        board[middle_top_col +1][middle_top_row +1]= top_left
    
        self.board= board
        self.rows= rows
        self.columns= columns
        self.turn= first
        self.game_type= game_type

    def print_board(self)-> None:
        '''Prints a visual representation of the board'''
        for row in range(self.columns):
            string2= '    '
            for column in range(self.columns):
                if self.board[column][row] == 0:
                    string2 += '.'
                elif self.board[column][row] == 'B':
                    string2 += 'B'
                else:
                    string2 += 'W'
                string2 += '  '
            print(string2)

    def count(self) -> dict:
        '''Counts how many of each piece are on the board, and returns a dictionary with the corresponding amounts'''
        black= 0
        white= 0
        result= {}
        for col in self.board:
            for space in col:
                if space == 'B':
                    black += 1
                elif space == 'W':
                    white += 1

        result['B'] = black
        result['W'] = white
        return result

    def board_status(self)-> str:
        '''Returns whether or no the board is filled with pieces or not'''
        board_status= 'FULL'
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                if self.board[col][row] == 0:
                    board_status= 'NOT FULL'

        return board_status

    def check_valid_move(self)-> str:
        '''Checks if there are any valid moves for the current players turn'''
        result= 'NO'
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                if make_move(self, col, row, 'NO')== 'VALID':
                    result= 'YES'

        return result

    def game_status(self)-> str:
        '''Checks if the game is over'''
        result= 'END'
        if self.board_status()== 'FULL':
            return 'END'
        else: 
            if self.check_valid_move() == 'NO':
                if self.turn== 'B':
                    self.turn= 'W'
                else:
                    self.turn= 'B'
                if self.check_valid_move() == 'NO':
                    return 'END'
                result= 'CONT'
            elif self.check_valid_move() == 'YES':
                result= 'CONT'

        return result

    def determine_winner(self) -> str:
        '''If the game is over, checks who the winner is depending on game type.'''
        
        if self.game_status() == 'END':
            if self.count()['B'] > self.count()['W']:
                if self.game_type == '>':
                    return 'B'
                else:
                    return 'W'
            elif self.count()['B'] < self.count()['W']:
                if self.game_type == '>':
                    return 'W'
                else:
                    return 'B'
            else:
                return 'NONE'
        else:
            return 'GAME NOT OVER'

