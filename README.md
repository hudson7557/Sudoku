# NP-Complete Puzzle - Sudoku 

        # while _solved is False 

        # look through the puzzle to find empty spaces. (for loop)

            # once you find an empty space check if it's in the memo table

                # if it's memoized set that list to possibe_nums

                # if it's not we copy a set of all possible solutions 
        
            #  iterate through list of possible numbers

                # if there is only one valid placement, place it 

                # if there is no valid placement skip it AND place possible
                # numbers in the memo table

        # run check_zero to set _solved