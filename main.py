from GameBoard import GameBoard
from Agent import Agent
import sys
import time

# Name: Elijah Atienza
# Date: 2/10/25
# Purpose: Main program housing game logic

if __name__ == "__main__":

    gameBoard = GameBoard()
    agentMain = Agent(gameBoard)
    divider = "\n=================================================\n"
    
    print(divider)
    print("Select the AI's opponent")
    print("[1] Human \n[2] AI")

    opponent = input("==> ")

    if opponent == "1":
        opponent = "Human"
        print("Starting a game against a human.")
        # Start a user vs AI game
    elif opponent == "2":
        opponent == "AI"
        agentOpp = Agent(gameBoard)
        print("Starting a game against the AI.")
        # Start an AI vs AI game
    else:
        print("Invalid choice. Please restart the program and select a valid option.")
        sys.exit(1)

    draw = False
    while(draw != True and gameBoard.checkWin() != True):
        # print board state and ask for players turns
        print(divider)
        gameBoard.print()

        print("\nPlayer {}'s turn... ".format(gameBoard.player))

        if(opponent == "Human" and gameBoard.player == 1):
            row = input("Enter row [0 to 2]: ")
            col = input("Enter col [0 to 2]: ")

            while(gameBoard.tryPlacePiece(gameBoard.player, row, col) != True):
                if(gameBoard.checkDraw()):
                    draw = True
                    break
                row = input("Enter row [0 to 2]: ")
                col = input("Enter col [0 to 2]: ")
        elif(opponent == "Human" and gameBoard.player == 2):
            print("Agent is thinking...")
            time.sleep(2)  #This is optional but I wanted to see my agents play in real time
            move = agentMain.agent_move()
        
        else:
            if(gameBoard.player == 1):
                print("Agent is thinking...")
                time.sleep(2)  #This is optional but I wanted to see my agents play in real time
                move = agentMain.agent_move()

            else:
                print("Agent is thinking...")
                time.sleep(2) 
                move = agentOpp.agent_move()

        #check for draw
        if(gameBoard.checkDraw()):
            draw = True
            break

        #switch player
        gameBoard.player = 2 if gameBoard.player == 1 else 1

    print(divider)

    gameBoard.print()

    if (draw == False):
        print(divider)

        gameBoard.player = 2 if gameBoard.player == 1 else 1
        print("Player {} WON!!!".format(gameBoard.player))
        gameBoard.player = 2 if gameBoard.player == 1 else 1
        print("Player {}, better luck next time!!".format(gameBoard.player))
    else:
        print(divider)

        print("TIE!!!!")
    
    print(divider)
            




    
    


    



    