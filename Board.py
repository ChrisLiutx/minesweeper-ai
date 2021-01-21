"""
Board.py

Stores the info of the board and mines.
"""
import random
import Cell

class Board:
    """
    Board that contains all the mines
    """

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.height = 0
        self.width = 0
        self.num_mines = 0
        self.end = False
        if self.difficulty == 0:
            self.height = 9
            self.width = 9
            self.num_mines = 10
        elif self.difficulty == 1:
            self.height = 16
            self.width = 16
            self.num_mines = 40
        elif self.difficulty == 2:
            self.height = 24
            self.width = 24
            self.num_mines = 99
        else:
            raise InputError(self.difficulty, "Choose only 0, 1 or 2.\n")

        self.size = self.height * self.width
        self.cells = []
        for row in range(self.height):
            r = []
            for col in range(self.width):
                r.append(Cell.Cell(row, col))
            self.cells.append(r)

    def generate_mines(self, start_r, start_c):

        starting = start_r * self.width + start_c
        choices = list(range(self.size))
        choices.remove(starting)
        for rand in random.sample(choices, self.num_mines):
            self.cells[rand//self.width][rand%self.width].set_mine()


    def print_board(self):
        print("\t=============")
        print("\t MINESWEEPER")
        print("\t=============\n")

        st = "   "
        for col in range(self.width):
            if col + 1 >= 10:
                st = st + "    " + str(col + 1)
            else:
                st = st + "     " + str(col + 1)
        print(st)

        for row in range(self.height):
            if row == 0:
                st = "     "
                for col in range(self.width):
                    st = st + " _____"
                print(st)

            st = "     "
            for col in range(self.width):
                st = st + "|     "
            print(st + "|")
            if row + 1 >= 10:
                st = " " + str(row + 1) + "  "
            else:
                st = "  " + str(row + 1) + "  "
            for col in range(self.width):
                st = st + "|  " + self.cells[row][col].get_display() + "  "
            print(st + "|")

            st = "     "
            for col in range(self.width):
                st = st + "|_____"
            print(st + "|")

        print("\n")

    def print_board_debug(self):
        print("\t=============")
        print("\t    DEBUG")
        print("\t=============\n")

        st = "   "
        for col in range(self.width):
            if col + 1 >= 10:
                st = st + "    " + str(col + 1)
            else:
                st = st + "     " + str(col + 1)
        print(st)

        for row in range(self.height):
            if row == 0:
                st = "     "
                for col in range(self.width):
                    st = st + " _____"
                print(st)

            st = "     "
            for col in range(self.width):
                st = st + "|     "
            print(st + "|")

            if row + 1 >= 10:
                st = " " + str(row + 1) + "  "
            else:
                st = "  " + str(row + 1) + "  "
            for col in range(self.width):
                st = st + "|  " + str(self.cells[row][col].get_value()) + "  "
            print(st + "|")

            st = "     "
            for col in range(self.width):
                st = st + "|_____"
            print(st + "|")

        print("\n")


    def set_values(self):
        """
        sets the value for each cell
        """

        for row in range(self.height):
            for col in range(self.width):
                cell = self.cells[row][col]
                if cell.is_mine():
                    cell.set_value(9)
                else:
                    if row > 0 and self.cells[row-1][col].is_mine():
                        cell.incr_value()
                    if row < self.height - 1 and self.cells[row+1][col].is_mine():
                        cell.incr_value()
                    if col > 0 and self.cells[row][col-1].is_mine():
                        cell.incr_value()
                    if col < self.width - 1 and self.cells[row][col+1].is_mine():
                        cell.incr_value()
                    if row > 0 and col > 0 and self.cells[row-1][col-1].is_mine():
                        cell.incr_value()
                    if row > 0 and col < self.width - 1 and self.cells[row-1][col+1].is_mine():
                        cell.incr_value()
                    if row < self.height - 1 and col > 0 and self.cells[row+1][col-1].is_mine():
                        cell.incr_value()
                    if row < self.height - 1 and col < self.width - 1 and self.cells[row+1][col+1].is_mine():
                        cell.incr_value()

    def action(self, action, row, col):
        """
        action taken by user
        f = flag
        u = uncover
        return "Error Message" if illegal move
        return -1 if uncovered mine
        return 0 if action completed
        """

        cell = self.cells[row-1][col-1]
        if action == "f":
            if cell.is_uncovered():
                return "Cannot flag uncovered cell.\n"
            elif cell.get_display() == " ":
                cell.set_display("F")
                print("Flagged cell at row " + str(row) + " col "+ str(col) + "\n")
            elif cell.get_display() == "F":
                cell.set_display(" ")
                print("UNFlagged cell at row "  + str(row) + " col "+ str(col) + "\n")
            else:
                return "Unknown error in action.\n"
            return 0
        elif action == "u":
            if cell.is_uncovered():
                return "Cell already uncovered.\n"
            elif cell.is_mine():
                print("Uncovered cell at row " + str(row) + " col "+ str(col) + "\n")
                self.end = True
                return -1
            else:
                self.check_cell(cell)
                return 0
        else:
            return "Invalid action. Please choose either f or u.\n"

    def check_cell(self, cell):
        row = cell.get_row()
        col = cell.get_col()
        print("Uncovered cell at row " + str(row + 1) + " col "+ str(col + 1) + "\n")
        val = cell.get_value()
        cell.set_display(str(val))
        cell.uncover()
        if val == 0:
            if row > 0 and not self.cells[row-1][col].is_uncovered():
                self.check_cell(self.cells[row-1][col])
            if row < self.height - 1 and not self.cells[row+1][col].is_uncovered():
                self.check_cell(self.cells[row+1][col])
            if col > 0 and not self.cells[row][col-1].is_uncovered():
                self.check_cell(self.cells[row][col-1])
            if col < self.width - 1 and not self.cells[row][col+1].is_uncovered():
                self.check_cell(self.cells[row][col+1])
            if row > 0 and col > 0 and not self.cells[row-1][col-1].is_uncovered():
                self.check_cell(self.cells[row-1][col-1])
            if row > 0 and col < self.width - 1 and not self.cells[row-1][col+1].is_uncovered():
                self.check_cell(self.cells[row-1][col+1])
            if row < self.height - 1 and col > 0 and not self.cells[row+1][col-1].is_uncovered():
                self.check_cell(self.cells[row+1][col-1])
            if row < self.height - 1 and col < self.width - 1 and not self.cells[row+1][col+1].is_uncovered():
                self.check_cell(self.cells[row+1][col+1])


    def check_win(self):
        if not self.end:
            count = 0
            for row in range(self.height):
                for col in range(self.width):
                    cell = self.cells[row][col]
                    if cell.is_uncovered():
                        count += 1
            if count == self.size - self.num_mines:
                self.end = True
                return True
        return False

    def reveal(self):
        for row in range(self.height):
            for col in range(self.width):
                cell = self.cells[row][col]
                if cell.is_mine():
                    cell.set_display("M")
                else:
                    cell.set_display(str(cell.get_value()))
        self.print_board()

    def is_end(self):
        return self.end

    def get_dimensions(self):
        return self.height, self.width
