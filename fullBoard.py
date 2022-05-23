from spaceCheck import *
def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
