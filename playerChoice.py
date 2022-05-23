from spaceCheck import space_check


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('choose a number between 1-10'))
    return position