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



    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
