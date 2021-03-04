# Scott Hudson
# CS 325 - Portfolio project
# Medium difficulty sudoku game which comes with a solver, GUI, and puzzle
# generator.

import random
import collections as collec  # used Counter to avoid sorting lists


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

        self._solved = False

        self._board = [[0, 2, 0, 1, 5, 0, 3, 0, 0],
                       [9, 6, 0, 3, 2, 0, 1, 4, 8],
                       [0, 4, 0, 6, 8, 9, 7, 0, 2],
                       [5, 9, 3, 4, 0, 0, 2, 7, 0],
                       [4, 7, 0, 5, 0, 3, 6, 8, 0],
                       [0, 1, 8, 9, 7, 0, 4, 0, 5],
                       [0, 0, 0, 2, 0, 5, 9, 1, 0],
                       [1, 5, 0, 7, 9, 6, 0, 0, 0],
                       [2, 0, 9, 8, 4, 0, 0, 6, 0]]

        self._starter_board = [[0, 2, 0, 1, 5, 0, 3, 0, 0],
                               [9, 6, 0, 3, 2, 0, 1, 4, 8],
                               [0, 4, 0, 6, 8, 9, 7, 0, 2],
                               [5, 9, 3, 4, 0, 0, 2, 7, 0],
                               [4, 7, 0, 5, 0, 3, 6, 8, 0],
                               [0, 1, 8, 9, 7, 0, 4, 0, 5],
                               [0, 0, 0, 2, 0, 5, 9, 1, 0],
                               [1, 5, 0, 7, 9, 6, 0, 0, 0],
                               [2, 0, 9, 8, 4, 0, 0, 6, 0]]

    # method to display the board
    def display(self):

        for i in range(len(self._board)):

            print(self._board[i])

        # print(self._solved)

    def fill_grid(self):

        has_zero = True

        while has_zero is True:

            # use shuffle to get a different order each time
            grid = [[0 for row in range(9)] for col in range(9)]

            random.shuffle(self._numbers)

            for number in self._numbers:

                for x in range(9):

                    for y in range(9):

                        if self.valid(grid, x, y, number) and grid[x][y] == 0:

                            grid[x][y] = number

            has_zero = self.contains_zero(grid)
            self._board = grid
            self.display()

        return grid

    def contains_zero(self):

        for i in range(9):

            for j in range(9):

                if self._board[i][j] == 0:

                    return True

        return False

    # method to see if a placement is valid
    def valid(self, row, col, number):

        valid = True

        # check to see if the column is valid
        for x in range(9):

            if self._board[x][col] == number:

                valid = False

        # check to see if the row is valid
        for y in range(9):

            if self._board[row][y] == number:

                valid = False

        # check to see if the mini-grid is valid
        mini_row = row // 3  # use floor because it will return a 0, 1, or 2
        mini_col = col // 3

        for x in range(3):

            for y in range(3):

                if self._board[mini_row * 3 + x][mini_col * 3 + y] == number:

                    valid = False

        return valid

    """
    Method used to place a number, it checks to make sure the number is valid
    for 9x9 sudoku, and that the position you are targeting is not from the
    original puzzel. It does not make sure the placement is valid thus allowing
    mistakes.
    """

    def place_number(self, row, col, number):

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

        # 0 is used to represent an empty space, since the starter board is
        # never manipulated, a zero tells us it's a changable space
        if self._board[row][col] == 0:

            # check whether the placement is legal
            if self.check_single_cell(row, col, number):

                # if placement is legal, do it and return True
                self._board[row][col] = number

                return True

        return False

    """
    Method used by check_solution to check each cell against the three rules.
    It will return True or False depending on what it finds.
    """

    def check_single_cell(self, row, col, number):

        # make sure the number is valid for 9x9 sudoku
        if number in self._numbers:

            # check to see if the column is valid
            for x in range(9):

                # check the location and skip the current number
                if self._board[x][col] == number and x != row:

                    return False

            # check to see if the row is valid
            for y in range(9):

                # check the location and skip the current number
                if self._board[row][y] == number and y != col:

                    return False

            # check to see if the mini-grid is valid
            mini_row = row // 3  # use floor to return a 0, 1, or 2
            mini_col = col // 3

            # loop through the three by three mini-grid
            for x in range(3):

                for y in range(3):

                    # calculate the current location once for x and y
                    curr_x = mini_row * 3 + x
                    curr_y = mini_col * 3 + y

                    # check if there is a duplicate number
                    if self._board[curr_x][curr_y] == number:

                        # make sure the number isn't our current number
                        if curr_x != row and curr_y != col:

                            return False

        return True

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
                if not self.check_single_cell(i, j, self._board[i][j]):

                    return False

        self._solved = True
        return True

    """
    Method used by check whether a completed game is correct or not by checking
    the four rules. It will return True or False depending on what it finds.
    """

    def verify_solution(self):

        # check each row
        for y in range(9):

            curr_row = []

            # add all numbers from a column to the column list
            for x in range(9):

                curr_row.append(self._board[x][y])

            # compare the two using the dictionary returned by Counter
            # if they're not the same something is wrong
            if collec.Counter(curr_row) != collec.Counter(self._numbers):

                return False

        # check each column
        for x in range(9):

            curr_col = []

            # add all numbers from a column to the column list
            for y in range(9):

                curr_col.append(self._board[x][y])

            # compare the two using the dictionary returned by Counter
            # if they're not the same something is wrong
            if collec.Counter(curr_col) != collec.Counter(self._numbers):

                return False

        # check each 3x3 grid
        for i in range(3):

            for j in range(3):

                curr_grid = []

                # loop through the three by three mini-grid
                for x in range(3):

                    for y in range(3):

                        # calculate the current location for x and y
                        curr_x = i * 3 + x
                        curr_y = j * 3 + y

                        curr_grid.append(self._board[curr_x][curr_y])

                # compare the two, if they're not the same something is wrong
                if collec.Counter(curr_grid) != collec.Counter(self._numbers):

                    return False

        return True

    """
    Method used to solve a sudoku puzzle using iteration and memoization to
    make assumptions and place numbers within the board. Purely of my own
    design I just wanted to see if I could solve the problem on my own and
    disregarded efficiency in this instance.
    """

    def solve(self):

        # table used for memoization, similar to a dp_table
        memo_table = [[[] for x in range(9)] for y in range(9)]

        # while the puzzle is not solved
        while self.contains_zero():

            # look through the puzzle to find empty spaces
            for x in range(9):

                for y in range(9):

                    # check if the empty space is in the memo table
                    if self._board[x][y] == 0:

                        curr_memo = memo_table[x][y]

                        # if it's not memoized set that list
                        if curr_memo == []:

                            curr_memo = self._numbers.copy()

                    remove_these = []

                    #  iterate through possible numbers to see what's valid
                    for i in range(len(curr_memo)):

                        # if a number is not valid it's stored to be removed
                        if not self.check_single_cell(x, y, curr_memo[i]):

                            remove_these.append(curr_memo[i])

                    # remove all the numbers which are not possible anymore
                    for i in range(len(remove_these)):

                        curr_memo.remove(remove_these[i])

                    # if there is only one valid placement, place it
                    if len(curr_memo) == 1:

                        self.place_valid_number(x, y, curr_memo[0])


if __name__ == "__main__":
    sudoku = grid()
    sudoku.display()
    sudoku.solve()
    print("HERE")
    # print(sudoku.place_number(0, 0, 1))
    sudoku.display()
    print("---")
    print(sudoku.verify_solution())
    print("---")
    sudoku.display()
