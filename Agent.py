from GameTree import GameTree

# Name: Elijah Atienza
# Date: 2/10/25
# Purpose: GameTree logic and functionality

class Agent:
    MAX_DEPTH = 3

    def __init__(self, game_board):
        self.game_board = game_board
    

    def agent_move(self):
        """
        purpose: Moves agent on the gameBoard
        
        logic: Expand children of the gameBoard and run minimax to find best move
        
        returns: 
            GameTree: A GameTree representing the best_move node. This node holds a best move for the agent.
        """
        root = GameTree(self.game_board, self.MAX_DEPTH)
        expanded_nodes = root.expand_children(self.MAX_DEPTH)

        while ((not self.game_board.checkDraw()) or (not self.game_board.checkWin())):
            best_child = root.run_minimax(root.depth, True)
            while (not (self.game_board.tryPlacePiece(self.game_board.player, best_child.move[0], best_child.move[1]))):
                if(self.game_over):
                    break
            print(best_child.move)
            print("Nodes Expanded = ", expanded_nodes)
            return best_child.move
        return False
    
    def game_over(self):
        """
        purpose: Check if the game is over
        
        logic: Checking if either a win state or draw state is met
        
        returns: 
            bool: A boolean value representing if the game is over
        """
        return self.game_board.checkWin() or self.game_board.checkDraw()
        