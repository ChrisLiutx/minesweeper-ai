"""
Cell.py

Individual Mine cells
"""

class Cell():

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.mine = False
        self.value = 0
        self.display = " "
        self.uncovered = False

    def set_mine(self):
        self.mine = True

    def get_row(self):
        return self.height

    def get_col(self):
        return self.width

    def is_uncovered(self):
        return self.uncovered

    def uncover(self):
        self.uncovered = True

    def get_value(self):
        """
        returns true value of cell

        -1 = Error
        0 to 8 = number of bombs around
        9 = mine
        """
        assert self.value >= 0
        assert self.value <= 9
        return self.value

    def get_display(self):
        """
        returns the display.

        E = Error
        0 to 8 = number of bombs around
        M = mine
        " " = hidden
        F = flagged
        """

        return str(self.display)

    def set_display(self, val):
        """
        Sets value of self.display
        """
        self.display = val

    def set_value(self, val):
        """
        sets the value
        """
        self.value = val

    def incr_value(self):
        self.value += 1

    def is_mine(self):
        """
        returns True if cell is mine, False otherwise
        """
        return self.mine
