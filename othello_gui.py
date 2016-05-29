#Project 5, Kevin Yin 29211757
#Othello GUI


import tkinter


from othello_logic import *


class UserDialog:
    def __init__(self):
        '''Initializes the User Dialog box, where the user can select game options'''

        self.font= ('Helvetica', 14)

        self.dialog_root= tkinter.Tk()

        welcome_label= tkinter.Label(master= self.dialog_root, text= 'Welcome to Othello!',
                                     font= ('Helvetica', 27) )

        welcome_label.grid(row= 0, column= 0, columnspan =2, padx= 10, pady= 10,
                       sticky= tkinter.N)

        row_label= tkinter.Label(master= self.dialog_root, text= 'Number of rows: ',font= self.font)
        row_label.grid(row=1, column= 0, padx= 10, pady= 10, sticky=tkinter.W)
        
        
        self.row_answer= tkinter.StringVar(self.dialog_root)
        self.row_answer.set(8)
        row_drop= tkinter.OptionMenu(self.dialog_root, self.row_answer, 4, 6, 8, 12, 14, 16)
        row_drop.grid(row=1, column=0, padx= 10, pady= 0.5, sticky= tkinter.E)

        col_label= tkinter.Label(master= self.dialog_root, text= 'Number of columns: ',font= self.font)
        col_label.grid(row=2, column= 0, padx= 10, pady= 10, sticky=tkinter.W)

        self.col_answer=tkinter.StringVar(self.dialog_root)
        self.col_answer.set(8)
        col_drop= tkinter.OptionMenu(self.dialog_root, self.col_answer, 4, 6, 8, 12, 14, 16)
        col_drop.grid(row=2, column=0, padx= 10, pady= 1, sticky= tkinter.E) 

        top_left_label= tkinter.Label(master= self.dialog_root,
                                      text= 'Top left piece: ',font= self.font)
        top_left_label.grid(row=3, column= 0, padx= 10, pady= 10, sticky=tkinter.W)

        self.top_left_answer= tkinter.StringVar(self.dialog_root)
        self.top_left_answer.set('B')
        top_left_drop= tkinter.OptionMenu(self.dialog_root, self.top_left_answer, 'B', 'W')
        top_left_drop.grid(row=3, column=0, padx= 10, pady= 1, sticky= tkinter.E)

        first_label= tkinter.Label(master= self.dialog_root,
                                      text= 'Piece that goes first: ',font= self.font)
        first_label.grid(row=4, column= 0, padx= 10, pady= 10, sticky=tkinter.W)

        self.first_answer= tkinter.StringVar(self.dialog_root)
        self.first_answer.set('B')
        first_drop= tkinter.OptionMenu(self.dialog_root, self.first_answer, 'B', 'W')
        first_drop.grid(row=4, column=0, padx= 10, pady= 1, sticky= tkinter.E)

        game_type_label= tkinter.Label(master= self.dialog_root,
                                      text= 'Game type: ',font= self.font)
        game_type_label.grid(row=5, column= 0, padx= 10, pady= 10, sticky=tkinter.W)

        self.game_type_answer= tkinter.StringVar(self.dialog_root)
        self.game_type_answer.set('>')
        game_type_drop= tkinter.OptionMenu(self.dialog_root, self.game_type_answer, '>', '<')
        game_type_drop.grid(row=5, column=0, padx= 10, pady= 1, sticky= tkinter.E)

        self.dialog_root.rowconfigure(0, weight= 2)
        self.dialog_root.rowconfigure(1, weight= 1)
        self.dialog_root.rowconfigure(2, weight= 1)
        self.dialog_root.rowconfigure(3, weight= 1)
        self.dialog_root.rowconfigure(4, weight= 1)
        self.dialog_root.rowconfigure(5, weight= 1)
        self.dialog_root.rowconfigure(6, weight= 1)
        self.dialog_root.columnconfigure(0, weight= 1)
        self.dialog_root.rowconfigure(1, weight= 1)

        button_begin= tkinter.Button(master = self.dialog_root, text = 'Begin the game!', font = ('Helvetica', 20),
                               command = self.on_button_pressed)
        button_begin.grid(row=6, column=0, padx= 10, pady= 10, sticky= tkinter.S)

    def on_button_pressed(self):
        '''Documents what happens when the user presses the 'Begin the game!' button'''

        columns= self.col_answer.get()
        rows= self.row_answer.get()
        top_left= self.top_left_answer.get()
        first= self.first_answer.get()
        game_type= self.game_type_answer.get()
        
        game= Gamestate(int(columns), int(rows), top_left, first, game_type)

        Othello(game)

        self.dialog_root.destroy()
        

    def start(self):
        self.dialog_root.mainloop()
        

class Othello:
    def __init__(self, game: 'Gamestate'):
        '''Initializes the Othello game GUI'''
        self.game= game

        self.vert_lines= self.game.columns
        self.horiz_lines= self.game.rows

        self.root = tkinter.Tk()
        self.canvas= tkinter.Canvas(master= self.root, width= 500, height= 450,
                                    background= 'green')
        self.canvas.grid(row= 2, column= 0, padx= 20, pady= 20,
                         sticky=tkinter.N + tkinter.S+ tkinter.W + tkinter.E)

        canvas_width= self.canvas.winfo_width()
        self.radius= (canvas_width / self.vert_lines) / 2
        self.canvas.bind('<Configure>', self.on_canvas_resized)
        self.canvas.bind('<Button-1>', self.on_canvas_clicked)

        title = tkinter.Label(master= self.root, text= 'Othello', font= ('Helvetica', 25))
        title.grid(row=0, column= 0, padx= 2, pady= 2, sticky=tkinter.N)

        self.root.rowconfigure(0, weight= 2)
        self.root.columnconfigure(0, weight= 1)
        self.root.rowconfigure(1, weight= 1)
        self.root.rowconfigure(2, weight= 1)
        self.root.rowconfigure(3, weight= 1)
        self.heading_text()

    def heading_text(self):
        '''Prints the heading text, which includes how many pieces are on the board and whos turn it is'''

        black_count= self.game.count()['B']
        white_count= self.game.count()['W']
        turn= self.game.turn
        
        black_label= tkinter.Label(master= self.root,
                                   text= 'B: '+ str(black_count), font= ('Helvetica', 14) )
        black_label.grid(row=1, column= 0, padx= 10, pady= 10, sticky=tkinter.W)
        white_label= tkinter.Label(master= self.root,
                                   text= 'W: '+ str(white_count), font= ('Helvetica', 14) )
        white_label.grid(row=1, column= 0, padx= 10, pady= 10, sticky=tkinter.E)
        turn_label= tkinter.Label(master= self.root,
                                   text= 'TURN: '+ turn, font= ('Helvetica', 14) )
        turn_label.grid(row=1, column= 0, padx= 10, pady= 10, sticky=tkinter.S)

        if self.game.game_status() == 'END':
            winner= self.game.determine_winner()
            
            end_label= tkinter.Label(master= self.root,
                                       text= 'WINNER: '+ winner , font= ('Helvetica', 14) )
            end_label.grid(row=3, column= 0, padx= 10, pady= 10, sticky=tkinter.S)

    def start(self):
        self.root.mainloop()

    def on_canvas_resized(self, event:tkinter.Event):
        '''Documents what happens when the board is resized'''
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        '''Draws the structure of the board onto the GUI'''
        self.canvas.delete(tkinter.ALL)

        canvas_width= self.canvas.winfo_width()
        canvas_height= self.canvas.winfo_height()

        mult= canvas_width / self.vert_lines
        mult1= canvas_height/ self.horiz_lines

        for x in range(self.vert_lines):
            self.canvas.create_line(mult* x, 0, mult*x, canvas_height)

        for x in range(self.horiz_lines):
            self.canvas.create_line(0,mult1*x , canvas_width, mult1*x)
        

    def on_canvas_clicked(self, event:tkinter.Event):
        '''Documents what occurs when the user clicks somewhere on the canvas'''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        mult_x= width / self.vert_lines
        mult_y= height/ self.horiz_lines


        click_x_pixel= event.x
        click_y_pixel= event.y

        for x in range(self.vert_lines):
            if click_x_pixel > x*mult_x:
                column= x

        for y in range(self.horiz_lines):
            if click_y_pixel > (y*mult_y):
                row= y
        make_move(self.game, column, row, 'YES')
        
        
        self.draw_pieces()
        self.heading_text()
        
    def draw_pieces(self):
        '''Draws all of the current pieces from the Gamestate object onto the game board GUI'''
        canvas_width= self.canvas.winfo_width()
        canvas_height= self.canvas.winfo_height()

        mult_x= canvas_width / self.vert_lines
        mult_y= canvas_height/ self.horiz_lines


        for col in range(len(self.game.board)):
            for row in range(len(self.game.board[col])):
                if self.game.board[col][row] == 'B':
                    self.canvas.create_oval(mult_x*col, mult_y*row, mult_x* (col+1),
                                            mult_y * (row+1), outline= 'gray', fill= 'black')
                elif self.game.board[col][row] == 'W':
                    self.canvas.create_oval(mult_x*col, mult_y*row, mult_x* (col+1),
                                            mult_y * (row+1), outline= 'gray', fill= 'white')
if __name__ == '__main__':
    UserDialog().start()
