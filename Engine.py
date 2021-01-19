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
    new_board.set_values()
    new_board.print_board()
    #new_board.print_board_debug()
    while not new_board.is_end():

        valid_input = False
        while not valid_input:
            usr_action = get_action()
            if usr_action == "exit":
                quit()
            usr_action = usr_action.split()
            if len(usr_action) != 3:
                print("Wrong number of inputs.\n")
            elif usr_action[0] not in ["0", "1"]:
                print("Invalid action. Please choose either 0 or 1.\n")
            elif not usr_action[1].isdigit():
                print("Row needs to be an integer\n")
            elif not usr_action[2].isdigit():
                print("Col needs to be an integer\n")
            else:
                result = new_board.action(int(usr_action[0]), int(usr_action[1]), int(usr_action[2]))
                if type(result) == int:
                    valid_input = True
                else:
                    print(result)
        if int(result) == -1:
            new_board.reveal()
            print("""
        ========================
            Sorry! YOU LOSE!
        ========================
            """)
        elif int(result) == 0:
            new_board.print_board()
            #new_board.print_board_debug()
        else:
            print("ERROR!")
        if new_board.check_win():
            new_board.reveal()
            print("""
        =================================
            Congratulations! YOU WIN!
        =================================
            """)


def get_action():
    print("""
=====================================================================
    Choose an action:
    [action] [row] [col]
    actions: f to flag, u to uncover
    eg: f 2 3
    this means I want to flag cell at row 2 column 3
=====================================================================
    """)
    return input("Please choose your option: \n")

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
            print("Weird error, please debug: \n")
            print(e)
            inp=input("")
            break

    quit()
else:
    print("Please run from Engine.py.\n")
