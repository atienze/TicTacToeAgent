# Name: Elijah Atienza
# Date: 2/10/25
# Purpose: GameBoard logic and functionality.

class GameBoard:

    # put these inside of a constructor to give the instance in my main class values when initializing.
    # to access elements: gameBoard[row][col] (THESE VALUES ARE BASED ON INDEX VALUES. START AT 0)
    def __init__(self):
        self.player = 1
        self.X = 'X' #Player 1 always
        self.O = 'O' #Player 2 always
        self.EMPTY = ' '
        self.gameBoard = [[self.EMPTY, self.EMPTY, self.EMPTY],
                          [self.EMPTY, self.EMPTY, self.EMPTY], 
                          [self.EMPTY, self.EMPTY, self.EMPTY]]
 
    
    def tryPlacePiece(self, player, row, col):
        """
        purpose: Moves an agent or player on the board while checking for necessary    cases such as the given coords are inbounds and not already occupied
        
        logic: Check all edge cases for user input and if the input is correct change the gameBoard to represent the move
        
        returns: 
            bool: Returns true if a piece is placed successfully, or false otherwise
        """
        try:
            row = int(row)
            col = int(col)
        except ValueError:
            print("Row and column must be integers, try again")
            return False
            
        if((row < 0 or row > 2) or (col < 0 or col > 2)):
            print("Invalid row or col value, try again")
            return False 
        if(GameBoard.checkDraw(self)):
            return False
        if(self.gameBoard[row][col] != self.EMPTY):
            print("That space is already occupied, try again.")
            return False
        if(player == 1):
            self.gameBoard[row][col] = self.X
        elif(player == 2):
            self.gameBoard[row][col] = self.O
        return True
    

    def checkWin(self):
        """
        purpose: Checks if the current state is in one of the 8 different win states for tic tac toe
        
        logic: Check rows, cols, and diagonals individually. If the row is a winner then the first value in the row/col/diag should be the same as the rest in the row/col/diag. 
        
        returns: 
            bool: Returns true if win state and False if not
        """

        symbol_cnt = 0

        # check the 3 rows for a winner
        for row in range(0,3):
            for col in range(0,3):
                symbol = self.gameBoard[row][0] 
                if (self.gameBoard[row][col] == symbol and symbol != self.EMPTY):
                    symbol_cnt += 1  #increment a counter for amount of same symbols seen
            if(symbol_cnt == 3):
                return True # someone won (whoever just went)
            symbol_cnt = 0

        # check the 3 cols for a winner
        for col in range(0,3):
            for row in range(0,3):
                symbol = self.gameBoard[0][col]
                if (self.gameBoard[row][col] == symbol and symbol != self.EMPTY):
                    symbol_cnt += 1
            if(symbol_cnt == 3):
                return True
            symbol_cnt = 0
                
        # check the 2 Diagonals for a winner
        #check values [0][0] == [1][1] == [2][2]
        #check values [0][2] == [1][1] == [2][0]
        back_cnt = 2
        for i in range (0, 3):
            symbol = self.gameBoard[0][0]
            if (self.gameBoard[i][i] == symbol and symbol != self.EMPTY):
                symbol_cnt += 1 
        if (symbol_cnt == 3):
            return True
        symbol_cnt = 0

        
        for j in range (0,3):
            symbol = self.gameBoard[0][2]
            if (self.gameBoard[j][back_cnt] == symbol and symbol != self.EMPTY):
                symbol_cnt += 1
            back_cnt-=1
        if (symbol_cnt == 3):
            return True
        symbol_cnt = 0

        # if all the win states are checked and no more valid spots to put a piece exist then it is a draw
        return False
    

    def checkDraw(self):
        """
        purpose: Checks if the current state is a draw
        
        logic: if gameBoard[0] && gameboard[1] && gameboard[2] are all full, each do not contain a single "EMPTY" instance, and there is no win state active then the game is a draw
        
        returns: 
            bool: Returns true if current state is draw and False if not
        """
        if(self.checkWin() != True): #if no one has won
            if((self.EMPTY not in self.gameBoard[0]) and #if no slot contains an "EMPTY"
               (self.EMPTY not in self.gameBoard[1]) and 
               (self.EMPTY not in self.gameBoard[2])):
                return True
        return False
    

    def print(self):
        """
        purpose: Prints out the formatted game board
        
        logic: print each row using .format syntax in a specific manner to create a UI
        
        returns: 
            None 
        """
        # The values in the gameBoard should only be accessed. 
        print(" {} | {} | {} ".format(
            self.gameBoard[0][0], 
            self.gameBoard[0][1], 
            self.gameBoard[0][2]
        ))
        print("---+---+---")
        print(" {} | {} | {} ".format(
            self.gameBoard[1][0], 
            self.gameBoard[1][1], 
            self.gameBoard[1][2]
        ))
        print("---+---+---")
        print(" {} | {} | {} ".format(
            self.gameBoard[2][0], 
            self.gameBoard[2][1], 
            self.gameBoard[2][2]
        ))
    

    def evaluate(self):
        """
        purpose: Setting up a heuristic function based on the state of the game board
        
        logic: Create 3 lists representing the rows, cols, and diagonals. The lists    are then used to plug valued into the heuristic function
        
        returns: 
            int: Returns a larger number if player 1 is at an advanrage and lower numbers if player 2 is at an advantage
        """

        X1 = X2 = O1 = O2 = 0

        row_arr = [[], [], []]
        col_arr = [[], [], []]
        diag_arr = [[], []]

        # fill the values into my arrays
        for i in range(3):
            for j in range(3):
                row_arr[i].append(self.gameBoard[i][j])
                col_arr[j].append(self.gameBoard[i][j])
                if i == j:
                    diag_arr[0].append(self.gameBoard[i][j])
                if i + j == 2:
                    diag_arr[1].append(self.gameBoard[i][j])
        
        # check the column array for winner
        for row in row_arr:
            if(row.count(self.X) == 2 and row.count(self.EMPTY)):
                X2 += 1
            if(row.count(self.X) == 1 and row.count(self.EMPTY) == 2):
                X1 += 1
            if(row.count(self.O) == 2 and row.count(self.EMPTY)):
                O2 += 1
            if(row.count(self.O) == 1 and row.count(self.EMPTY) == 2):
                O1 += 1

        # check the column array for winner
        for col in col_arr:
            if(col.count(self.X) == 2 and col.count(self.EMPTY)):
                X2 += 1
            if(col.count(self.X) == 1 and col.count(self.EMPTY) == 2):
                X1 += 1
            if(col.count(self.O) == 2 and col.count(self.EMPTY)):
                O2 += 1
            if(col.count(self.O) == 1 and col.count(self.EMPTY) == 2):
                O1 += 1

        # check the diagonal array for winner
        for diag in diag_arr:
            if(diag.count(self.X) == 2 and diag.count(self.EMPTY)):
                X2 += 1
            if(diag.count(self.X) == 1 and diag.count(self.EMPTY) == 2):
                X1 += 1
            if(diag.count(self.O) == 2 and diag.count(self.EMPTY)):
                O2 += 1
            if(diag.count(self.O) == 1 and diag.count(self.EMPTY) == 2):
                O1 += 1

        return 3 * X2 + X1 - (3 * O2 + O1)

    def clone(self):
        """
        purpose: Clones the current game board
        
        logic: Create a new instance of a gameboard and copy the data from the current game board
        
        returns: 
            GameBoard: A GameBoard representing a clone of the current game board
        """
        clone = GameBoard()
        clone.player = self.player
        clone.gameBoard = [row[:] for row in self.gameBoard]
        return clone

        
    
