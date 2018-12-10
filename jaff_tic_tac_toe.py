def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('-- --- --')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('-- --- --')
    print(f'{board[7]} | {board[8]} | {board[9]}')

def player_input():
    player1 = input('Player 1, please choose a marker X or O: ').upper()
    while player1 != 'X' and player1 != 'O':
        player1 = input('Stop playing around, this isnt a game, choose X or O: ').upper()
    if player1 == 'X':
        print('Player 1, you are Xpected to do well, heh.')
        player2 = 'O'
        return (player1,player2)
    elif player1 == 'O':
        print('Player 1, O-m-g, you be O this time around.')
        player2 = 'X'
        return (player1,player2)


def place_marker(board,marker,position):
    board[position] = marker

#place_marker(test_board,'$',8)
#print(display_board(test_board))

def win_check(board,mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    else:
        return False

import random
def choose_first():
    num = random.randint(1,2)
    if num == 1:
        print('Player1, you go first!')
        return True
    else:
        print('Player2, you go first!')
        return False

def space_check(board,position):
    return board[position] != 'X' or board[position] != 'O'

def full_board_check(board):
    for xo in range(1,10):
        if board[xo] == 'X'.upper() or board[xo] == 'O'.upper():
            continue
        else:
            return False
    return True

def player_choice(board):
    spot = int(input('Please select a position from 1-9: '))
    while spot < 1 or spot > 9:
        spot = int(input('Please select a position from 1-9: '))
    if space_check(test_board,spot):
        return spot

def replay():
    yn = input('Would you like to play again?\n "Y" for yes or "N" for no: ').upper()
    while yn != 'Y' and yn != 'N':
        yn = input("Bruh you gotta press 'y' or 'n'").upper()
    return yn == 'Y'

game_initiate = True
while game_initiate:
    print('Welcome to Tic Tac Toe!')
    test_board = [' ','1','2','3','4','5','6','7','8','9']
    display_board(test_board)
    marker = player_input()
    game_on = True
    #print(player)
    while game_on:
        #Player 1 Turn
        if choose_first == True:
            print("Player1, it's your turn")
            p1position = player_choice(test_board)
            place_marker(test_board,marker[0],p1position)
            display_board(test_board)
            if win_check(test_board,marker[0]):
                print("Player 1, you've won the game!")
                game_on = False
            elif full_board_check(test_board):
                print("All tied up!")
                game_on = False
            choose_first = False
        
        #Player2's turn.
        else:
            print("Player2, your move")
            p2position = player_choice(test_board)
            place_marker(test_board,marker[1],p2position)
            display_board(test_board)
            if win_check(test_board,marker[1]):
                print("Player 2, you've won the game!")
                game_on = False
            elif full_board_check(test_board):
                print("All tied up!")
                game_on = False
            choose_first = True
    if not replay():
        game_initiate = False
print("Thanks for playing!")
