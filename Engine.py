"""
Engine.py

Minesweeper game created by Chris Liu @ 2021
"""
import Board
import Cell

def run():
    print("Welcome to Chris's Minesweeper! Type exit at any time to end game.\n")

    print("""Difficulty levels:
    0. Beginner: 9 x 9 Board, 10 Mines
    1. Intermediate: 16 x 16 Board, 40 Mines
    2. Advanced: 24 x 24 Board, 99 Mines
    """)
    inp = -1
    while not inp in ["0", "1", "2"]:
        inp = input("Please enter 0, 1 or 2 for difficulty level. eg: 0\n")
        if inp == "exit":
            quit()
    inp = int(inp)
    new_board = Board.Board(inp)
    new_board.print_board()
    start_a, start_r, start_c = get_action(new_board)
    new_board.generate_mines(start_r-1, start_c-1)
    new_board.set_values()
    new_board.action(start_a, start_r, start_c)
    if new_board.check_win():
        win(new_board)
    else:
        new_board.print_board()
        #new_board.print_board_debug()
    while not new_board.is_end():

        valid_input = False
        while not valid_input:
            act = get_action(new_board)
            result = new_board.action(*act)
            if type(result) == int:
                valid_input = True
            else:
                print(result)

        if int(result) == -1:
            lose(new_board)
        elif int(result) == 0:
            new_board.print_board()
            #new_board.print_board_debug()
        else:
            print("ERROR!")
        if new_board.check_win():
            win(new_board)

def win(board):
    board.reveal()
    print("""
        =================================
            Congratulations! YOU WIN!
        =================================

                                   .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\\'.   '
      *            *..*         :
       *
        *

    """)

def lose(board):
    board.reveal()
    print("""
        ========================
            Sorry! YOU LOSE!
        ========================

             _.-^^---....,,--
         _--                  --_
        <                        >)
        |                         |
         \._                   _./
            ```--. . , ; .--'''
                  | |   |
               .-=||  | |=-.
               `-=#$%&%$#=-'
                  | ;  :|
         _____.,-#%&$@%#&#~,._____

    """)



def get_action(board):
    valid = False
    while not valid:
        print("""
    =====================================================================
        Choose an action:
        [action] [row] [col]
        actions: f to flag, u to uncover
        eg: f 2 3
        this means I want to flag cell at row 2 column 3
    =====================================================================
        """)
        usr_action = input("Please choose your option: \n")
        if usr_action == "exit":
            quit()
        usr_action = usr_action.split()
        if len(usr_action) != 3:
            print("Wrong number of inputs.\n")
        elif usr_action[0] not in ["f", "u"]:
            print("Invalid action. Please choose either f or u.\n")
        elif not usr_action[1].isdigit():
            print("Row needs to be an integer\n")
        elif not usr_action[2].isdigit():
            print("Col needs to be an integer\n")
        else:
            row = int(usr_action[1])
            col = int(usr_action[2])
            r = row - 1
            c = col - 1
            h, w = board.get_dimensions()
            if not (r >= 0 and r < h and c >= 0 and c < w):
                print("Invalid cell.\n")
            else:
                valid = True
    return usr_action[0], row, col

if __name__ == "__main__":
    print("Starting Minesweeper...\n")
    done = False
    while not done:
        try:
            run()
            inp = input("Start a new game?(y/n): \n")
            if inp == "n":
                done = True
        except Exception as e:
            print("Weird error, please contact mail@chrisliu.io: \n")
            print(e)
            inp=input("")
            break

    quit()
else:
    print("Please run from Engine.py.\n")
