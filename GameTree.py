from collections import deque
import random

# Name: Elijah Atienza
# Date: 2/10/25
# Purpose: GameTree logic and functionality

class GameTree:
    all_possible_moves = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

    def __init__(self, game_board, depth):
        self.children = deque()
        self.game_board = game_board
        self.MAX_DEPTH = 3
        self.move = ()
        self.nodes_expanded = 0
        self.depth = depth
        self.minimax_value = 0


    def expand_children(self, depth_limit):
        """
        purpose: Expands game tree to the given depth limit while filling in game tree nodes for the minimax algorithm to run on
        
        logic: Recursively clone and add a game board to the deque for every iteration of a new valid move while keeping track of nodes expanded
        
        returns: 
            int: Amount of nodes expanded and moves added to the deque
        """
        nodes_expanded = 0
        for move in self.find_valid_moves():
            nodes_expanded += 1
            clone = self.game_board.clone()
            clone.tryPlacePiece(clone.player, move[0], move[1]) # shouldnt need to check a return bool bc the move should be valid already
            tree = GameTree(clone, depth_limit - 1)
            tree.move = move
            self.children.append(tree)
            if depth_limit > 1:
                nodes_expanded += tree.expand_children(depth_limit - 1) #Recursively search the tree finding all the nodes at each level
        return nodes_expanded

        # AT THIS POINT ALL VALID MOVES THAT I CAN MAKE SHOULD BE STORED AS GameTreeNodes in my deque. I can now call minimax on my deque


    def run_minimax(self, depth, max_player):
        """
        purpose: Runs minimax on the game tree rooted at this node. 
        
        logic: Recursively go down the children in the deque that should have been added through the expand_children function
        
        returns: 
            GameTree: Returns a game tree child node that maximizes or minimizes the desired result
        """
        # Base case: Leaf node or Max Depth
        if (depth == 0 or self.game_board.checkWin() or self.game_board.checkDraw()):
            self.minimax_value = self.game_board.evaluate()
            return self

        best_children = [] # List to hold all children with the "best" value found so far

        if (max_player):
            maxEval = float('-inf')
            
            for child in self.children:
                # Recursive call
                eval_node = child.run_minimax(depth - 1, False)
                
                if eval_node.minimax_value > maxEval:
                    # Found a strictly better move: Clear list and add this one
                    maxEval = eval_node.minimax_value
                    best_children = [child]
                elif eval_node.minimax_value == maxEval:
                    # Found a move just as good as the best: Add to list
                    best_children.append(child)
            
            # Assign the value to this node
            self.minimax_value = maxEval
            
            # Pick a random move from the best options
            return random.choice(best_children) if best_children else None

        else: # Minimizing player
            minEval = float('inf')
            
            for child in self.children:
                # Recursive call
                eval_node = child.run_minimax(depth - 1, True)
                
                if eval_node.minimax_value < minEval:
                    # Found a strictly better move (lower is better for min)
                    minEval = eval_node.minimax_value
                    best_children = [child]
                elif eval_node.minimax_value == minEval:
                    # Found a move just as good: Add to list
                    best_children.append(child)
            
            # Assign the value to this node
            self.minimax_value = minEval
            
            # Pick a random move from the best options
            return random.choice(best_children) if best_children else None

    def find_valid_moves(self): 
        """
        purpose: Find all valid moves that exist for a current game board
        
        logic: iterate a list of all possible moves and attempt them on the current game board 

        returns: 
            list: Returns a list of all valid moves at a given game board
        """
        all_valid_moves = []

        for move in self.all_possible_moves:
            row = move[0]
            col = move[1]
            if(self.game_board.gameBoard[row][col] == self.game_board.EMPTY):
                all_valid_moves.append(move)
        
        return all_valid_moves
