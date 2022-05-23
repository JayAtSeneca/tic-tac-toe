from chooseFirst import *
from displayBoard import *
from placeMarker import *
from fullBoard import *
from playerChoice import *
from playerInput import *
from replay import *
from spaceCheck import *
from winCheck import *

print('Welcome to TIC TAC TOE!')
while True:
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker,position )

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! you have won the game!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_board(theBoard)
                    print('The game is Draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_board(theBoard)
                    print('The game is draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break

