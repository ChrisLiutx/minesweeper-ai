"""
AI.py

Ai class that solves the minesweeper automatically.
"""

class Bot:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.bot_cells = []
        for row in range(self.height):
            temp_row = []
            for col in range(self.width):
                temp_row.append(Bot_cell(row, col))
            self.bot_cells.append(temp_row)

        self.flag_actions = []
        self.uncover_actions = []

    def get_cell(self, row, col):
        return self.bot_cells[row][col]

    def get_action(self, board):
        displays = board.get_displays()
        for row in range(self.height):
            for col in range(self.width):
                bot_cell = self.bot_cells[row][col]
                bot_cell.update_cell(displays[row][col])
        if len(self.flag_actions) != 0:
            a = self.flag_actions.pop()
            return "f", a.get_row() + 1, a.get_col() + 1
        elif len(self.uncover_actions) != 0:
            a = self.uncover_actions.pop()
            return "u", a.get_row() + 1, a.get_col() + 1
        else:
            ss_result = self.simple_solver()
            if len(ss_result) != 0:
                if ss_result[0] == "f":
                    self.flag_actions = ss_result[1:]
                    a = self.flag_actions.pop()
                    return "f", a.get_row() + 1, a.get_col() + 1
                elif ss_result[0] == "u":
                    self.uncover_actions = ss_result[1:]
                    a = self.uncover_actions.pop()
                    return "u", a.get_row() + 1, a.get_col() + 1
        return ""





    def simple_solver(self):
        for row in range(self.height):
            for col in range(self.width):
                bot_cell = self.bot_cells[row][col]
                if not bot_cell.is_mine():
                    if bot_cell.get_value() != " ":
                        tot_mines = int(bot_cell.get_value())
                        num_mines = 0
                        num_clear = 0
                        num_unclear = 0
                        unclear_cells = []
                        if row > 0:
                            temp_cell = self.bot_cells[row-1][col]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if row < self.height - 1:
                            temp_cell = self.bot_cells[row+1][col]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if col > 0:
                            temp_cell = self.bot_cells[row][col-1]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if col < self.width - 1:
                            temp_cell = self.bot_cells[row][col+1]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if row > 0 and col > 0:
                            temp_cell = self.bot_cells[row-1][col-1]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if row > 0 and col < self.width - 1:
                            temp_cell = self.bot_cells[row-1][col+1]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if row < self.height - 1 and col > 0:
                            temp_cell = self.bot_cells[row+1][col-1]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if row < self.height - 1 and col < self.width - 1:
                            temp_cell = self.bot_cells[row+1][col+1]
                            if temp_cell.is_mine():
                                num_mines += 1
                            elif temp_cell.get_value() != " ":
                                num_clear += 1
                            else:
                                num_unclear += 1
                                unclear_cells.append(temp_cell)
                        if num_unclear != 0:
                            if num_unclear + num_mines == tot_mines:
                                #flag all unclear
                                for cell in unclear_cells:
                                    cell.flag()
                                return ["f"] + unclear_cells
                            elif num_mines == tot_mines:
                                return ["u"] + unclear_cells
        return []

class Bot_cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.val = " "
        self.mine = False

    def update_cell(self, val):
        self.val = val

    def get_value(self):
        return self.val

    def is_mine(self):
        return self.mine

    def flag(self):
        self.mine = True

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col
