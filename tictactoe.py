"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO =0
    for row in board:
        for item in row:
            if item == X:
                countX +=1
            elif item == O:
                countO += 1
   
    return X if countX <= countO else O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #My thoughts: Just see how many None are there, these are possible actions!
    possibleActions = set()
    for row in range(len(board)):
        for column in range (len(board[row])):
            if board[row][column] == None:
                possibleActions.add((row,column))
    return possibleActions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    while board[i][j] != EMPTY:
        print("Already occupied! Choose another slot.")
        try:
            i, j = tuple(map(int, input("Add the correct coordinates now (i, j): ").split(',')))
        except ValueError:
            print("Invalid input! Enter two integers separated by a comma.")
    playerCharacter = player(board)
    newBoard = [row[:] for row in board]
    newBoard[i][j] = playerCharacter
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:  #for 3 row checking
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None: # for 3 columns checking
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None: #for left and right diagonal
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    raise NotImplementedError
def isGameOver( board):
    for row in board:
        for cell in row:  #if game is still not over 
            if cell is None:
                return False 
    return True  

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:  #for 3 row checking
            return True
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None: # for 3 columns checking
            return True
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None: #for left and right diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return True
    
    if isGameOver(board) == False:
        return False
            
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        playerWhoWonGame = winner(board)
        if playerWhoWonGame == "X":
            return 1
        elif playerWhoWonGame == "O":
            return -1
        else:
            return 0 
# If the game has not ended yet, return None
    return None
    

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
