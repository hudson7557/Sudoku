# Scott Hudson
# CS 325 - Portfolio project
# Medium difficulty sudoku game which comes with a solver, GUI, and puzzle
# generator.

import random


"""
A class which is used to store and maintain a sudoku game board
"""


class grid:

    # class constructor
    def __init__(self):
        self._numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._solution_board = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
                                [9, 6, 5, 3, 2, 7, 1, 4, 8],
                                [3, 4, 1, 6, 8, 9, 7, 5, 2],
                                [5, 9, 3, 4, 6, 8, 2, 7, 1],
                                [4, 7, 2, 5, 1, 3, 6, 8, 9],
                                [6, 1, 8, 9, 7, 2, 4, 3, 5],
                                [7, 8, 6, 2, 3, 5, 9, 1, 4],
                                [1, 5, 4, 7, 9, 6, 8, 2, 3],
                                [2, 3, 9, 8, 4, 1, 5, 6, 7]]

        self._board = [[0, 2, 7, 1, 5, 4, 3, 9, 6],
                       [9, 6, 5, 3, 2, 7, 1, 4, 8],
                       [3, 4, 1, 6, 8, 9, 7, 5, 2],
                       [5, 9, 3, 4, 6, 8, 2, 7, 1],
                       [4, 7, 2, 5, 1, 3, 6, 8, 9],
                       [6, 1, 8, 9, 7, 2, 4, 3, 5],
                       [7, 8, 6, 2, 3, 5, 9, 1, 4],
                       [1, 5, 4, 7, 9, 6, 8, 2, 3],
                       [2, 3, 9, 8, 4, 1, 5, 6, 7]]

        self._starter_board = [[0, 2, 7, 1, 5, 4, 3, 9, 6],
                               [9, 6, 5, 3, 2, 7, 1, 4, 8],
                               [3, 4, 1, 6, 8, 9, 7, 5, 2],
                               [5, 9, 3, 4, 6, 8, 2, 7, 1],
                               [4, 7, 2, 5, 1, 3, 6, 8, 9],
                               [6, 1, 8, 9, 7, 2, 4, 3, 5],
                               [7, 8, 6, 2, 3, 5, 9, 1, 4],
                               [1, 5, 4, 7, 9, 6, 8, 2, 3],
                               [2, 3, 9, 8, 4, 1, 5, 6, 7]]

    # method to display the board
    def display(self):

        for i in range(len(self._board)):

            print(self._board[i])

    def fill_grid(self):

        has_zero = True

        while has_zero is True:

            # use shuffle to get a different order each time
            grid = [[0 for row in range(9)] for col in range(9)]

            random.shuffle(self._numbers)

            for number in self._numbers:

                for x in range(9):

                    for y in range(9):

                        if self.valid(grid, x, y, number) is True and grid[x][y] == 0:

                            grid[x][y] = number

            has_zero = self.contains_zero(grid)
            self._board = grid
            self.display()

        return grid

    def contains_zero(self, grid):

        for i in range(9):

            for j in range(9):

                if grid[i][j] == 0:

                    return True

        return False

    """
    Method used to place a number, it checks to make sure the number is valid
    for 9x9 sudoku, and that the position you are targeting is not from the
    original puzzel. It does not make sure the placement is valid thus allowing
    mistakes.
    """

    def place_number(self, row, col, number):

        # make sure the number is valid for 9x9 sudoku
        if number in self._numbers:

            # 0 is used to represent an empty space, since the starter board is
            # never manipulated, a zero tells us it's a changable space
            if self._starter_board[row][col] == 0:

                # if placement is legal, do it and return True
                self._board[row][col] = number

                return True

        return False

    """
    Method used to place a number, it checks to make sure the number is valid
    for 9x9 sudoku and then checks to make sure the placement is valid, if a
    placement is valid then it goes through, if not then it isn't allowed.
    """

    def place_valid_number(self, row, col, number):

        # make sure the number is valid for 9x9 sudoku
        if number in self._numbers:

            # 0 is used to represent an empty space, since the starter board is
            # never manipulated, a zero tells us it's a changable space
            if self._starter_board[row][col] == 0:

                # check whether the placement is legal
                if self.check_single_cell(row, col, number) is True:

                    # if placement is legal, do it and return True
                    self._board[row][col] = number

                    return True

        return False

    """
    Method used to iterate through a board, it calls check_single_cell on each
    cell and determines whether a completed game and soultion is correct.
    """

    def check_solution(self):

        # loop through the 9x9 board
        for i in range(9):

            for j in range(9):

                # call the check_single_cell method and return false if a
                # invalid placement is made
                if self.check_single_cell(i, j, self._board[i][j]) is False:

                    return False

        return True

    """
    Method used by check_solution to check each cell against the three rules.
    It will return True or False depending on what it finds.
    """

    def check_single_cell(self, row, col, number):

        # check to see if the column is valid
        for x in range(9):

            # check the location and skip the number we're currently evaluating
            if (self._board[x][col] == number and x != row):

                return False

        # check to see if the row is valid
        for y in range(9):

            # check the location and skip the number we're currently evaluating
            if (self._board[row][y] == number and y != col):

                return False

        # check to see if the mini-grid is valid
        mini_row = row // 3  # use floor because it will return a 0, 1, or 2
        mini_col = col // 3

        # loop through the three by three mini-grid
        for x in range(3):

            for y in range(3):

                # calculate the current location once for x and y
                curr_x = mini_row * 3 + x
                curr_y = mini_col * 3 + y

                # check if there is a duplicate number
                if (self._board[curr_x][curr_y] == number):

                    # make sure the number isn't our current number
                    if (curr_x != row and curr_y != col):

                        return False

        return True

    # method to see if a placement is valid
    def valid(self, row, col, number):

        valid = True

        # check to see if the column is valid
        for x in range(9):

            if (self._board[x][col] == number):

                valid = False

        # check to see if the row is valid
        for y in range(9):

            if (self._board[row][y] == number):

                valid = False

        # check to see if the mini-grid is valid
        mini_row = row // 3  # use floor because it will return a 0, 1, or 2
        mini_col = col // 3

        for x in range(3):

            for y in range(3):

                if (self._board[mini_row * 3 + x][mini_col * 3 + y] == number):

                    valid = False

        return valid


if __name__ == "__main__":
    sudoku = grid()
    sudoku.display()
    print(sudoku.place_number(0, 0, 7))
    sudoku.display()
    print(sudoku.place_number(0, 0, 8))
    sudoku.display()
    print(sudoku.place_valid_number(0, 0, 4))
