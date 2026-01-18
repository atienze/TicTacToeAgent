# Tic-Tac-Toe AI Agent

A robust Tic-Tac-Toe AI implemented in Python using the Minimax algorithm. This project demonstrates object-oriented design, recursive game tree search, and heuristic evaluation.
## Overview

This project implements a classic Tic-Tac-Toe game where an AI agent determines the optimal move to make against a player (or another agent). It uses a GameTree structure to look ahead at possible future board states and selects the path that maximizes its chances of winning while minimizing the opponent's.

## Key Features

* **Minimax Algorithm:** The agent uses a depth-limited Minimax search to calculate the best possible move.
* **Heuristic Evaluation:** A custom scoring function evaluates board states based on the advantage of rows, columns, and diagonals.
* **Object-Oriented Design:** Clean separation of concerns between the Agent, GameBoard, and GameTree logic.
* **Console Interface:** Simple, text-based visualization of the game board.

## Code Structure

### 1. Agent
The "brain" of the operation. It manages the AI's turn by instantiating a GameTree and triggering the Minimax algorithm.

### 2. GameTree
Handles the recursive search logic.

### 3. GameBoard
Manages the state of the game.

## Getting Started

### Prerequisites
* Python 3.x installed on your machine.

### Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/tictactoe-ai.git](https://github.com/yourusername/tictactoe-ai.git)
    cd tictactoe-ai
    ```

2.  **Run the program**
    ```bash
    python3 main.py
    ```

## Example Output

The board is rendered in the console as follows:

```text
 X | O |   
---+---+---
   | X |   
---+---+---
 O |   |
