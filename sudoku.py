# Scott Hudson
# CS 325 - Portfolio project
# Medium difficulty sudoku game which comes with a solver, GUI, and puzzle
# generator.

import collections as collec  # used Counter to avoid sorting lists


"""
A class which is used to store and maintain a sudoku game board
"""


class grid:

    """
    Class constructor used to maintain a sudoku board, validate input, and
    track state.
    """
    def __init__(self):
        self._numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

        self._helper_on = False

    """
    Tester method to display the board line by line.
    """
    def display(self):

        for i in range(len(self._board)):

            print(self._board[i])

    """
    Method used to get input from the user, it calls certain functions
    depending on what it recieves as input and validates input.
    """

    def get_input(self):

        # display the prompt and capture user input
        user_command = input("Please enter the row, column, and number: ")

        # remove any excess white space
        user_command.strip()

        # Helper results in a call to the togglehelper method
        if user_command == "Helper":

            self.toggle_helper()

        # Solve results in a call to the solve method
        elif user_command == "Solve":

            self.solve()

        # if the input isn't one of our methods we process it
        else:

            # split it into an array to make life easy
            command_array = user_command.split(",")

            # give these initial values to allow try to work
            row = 0
            col = 0
            num = 0

            # try to assign values
            try:
                # row and col are the input minus 1 to adjust from the user
                # index to array indexing
                row = int(command_array[0].strip()) - 1

                col = int(command_array[1].strip()) - 1

                num = int(command_array[2].strip())

            # if there weren't enough numbers input
            except IndexError:

                print("*Not enough numbers provided.")

            # if a int wasn't entered
            except ValueError:

                print("*Opps, please enter valid numbers.")

            # if either of the above exceptions occurs, the values will have
            # their initial value, we catch that and return.
            if (row, col, num) == (0, 0, 0):

                return

            # if helper is on we use place_valid_number to ensure mistakes
            # can't be made
            if self._helper_on:

                self.place_valid_number(row, col, num)

            # if helper is off we use place_number
            else:

                self.place_number(row, col, num)

    """
    Method to toggle whether helper is on or not, it displays the current state
    """

    def toggle_helper(self):

        self._helper_on = not self._helper_on

        if self._helper_on:

            print("Helper is now on, you will not be able to place \
incorrect numbers.")

        elif not self._helper_on:

            print("Helper is now off, you will be able to place incorrect \
numbers.")

    """
    Method to determine whether the board has any empty spaces in it which are
    represented by a zero.
    """

    def contains_zero(self):

        for i in range(9):

            for j in range(9):

                if self._board[i][j] == 0:

                    return True

        return False

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

        else:

            print("This space has a starter number and cannot be overwritten!")

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

        else:

            print("This space has a starter number and cannot be overwritten!")

        return False

    """
    Method used to display the board in a 9x9 grid in the CLI
    """

    def print_board(self):

        header = "       1   2   3   4   5   6   7   8   9"

        bar = "      -----------------------------------"

        print()
        print(header)
        print()

        # put the lines together from the array
        for i in range(len(self._board)):

            # add index number to the display
            line = str(i + 1)

            # bars are used for styling
            line = line + "    | "

            # add each cell to the line
            for j in range(len(self._board)):

                line = line + str(self._board[i][j]) + " | "

            # print a bar and then the line
            print(bar)
            print(line)

        # cap it off with another bar and white space
        print(bar)
        print()

    """
    Method used to check if a number is valid in a cell or not, it's part of
    place_valid_number and doesn't allow the user to place erronius numbers.
    It is losely based off of answers to Algorithm for solving Sudoku post on
    stack exchange. Though I changed a lot because I thought most of them were
    pretty bad.
    https://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku
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

                print("A number is wrong, please try again")

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

                print("A number is wrong, please try again")

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

                    print("A number is wrong, please try again")

                    return False

        print("Solved correctly, nice work!")

        self._solved = True

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

        self._board = self._starter_board.copy()

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

                        self.place_number(x, y, curr_memo[0])

        self.print_board()


if __name__ == "__main__":

    sudoku = grid()

    print("---Welcome to command line sudoku!---")
    print()
    print("You can toggle whether the game allows you to make a mistake \
or not by entering the command 'Helper'")
    print()
    print("You can solve the puzzle at any time by enterning 'Solve'")
    print()
    print("Please enter the column number and row you would like to place \
the number in followed by the number you would like to place seperated by \
commas and spaces.")
    print("You can use the grid numbers around the board to track the index.")
    print("It should look something like this, '1, 1, 5'")
    print()

    while not sudoku._solved:

        sudoku.print_board()

        sudoku.get_input()

        if not sudoku.contains_zero():

            sudoku.verify_solution()
