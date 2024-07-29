import random


def display_board(board):  # This is how our board will look like. Each index 1-9 corresponds with a number on a number pad.
    print(board[7] + '|' + board[8] + '|' + board [9])
    print(board[4] + '|' + board[5] + '|' + board [6])
    print(board[1] + '|' + board[2] + '|' + board [3])


def player_input():  # This function takes the first player input and assign their marker as 'X' or 'O'
    marker = ''

    while not (marker == 'X' or marker == 'O'):  # This while loop will continue to iterate until you provide a correct answer (X or O).
        marker = input('Player 1: Do you want to be X or O?').upper()

    return ('X', 'O') if marker == 'X' else ('O', 'X')


def place_marker(board, marker, position):  # This function assigns player's desired position (1-9) using indexing
    board[position] = marker


def win_check(board,mark):  # all winning scenarios
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():  # This function randomly chooses who starts first
    return 'Player 2' if random.randint(0, 1) == 0 else 'Player 1'


def space_check(board, position):  # This function returns a boolean indicating whether a space on the board is freely available.
    return board[position] == ' '


def full_board_check(board):  # This function checks if the board is full and returns a boolean value
    for i in range (1,10):

        if space_check(board,i):
            return False  # if board is not full

    return True  # if board is full


def player_choice(board):  # This function asks for player's next position
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):  # This loop will continue to iterate until we provide a correct input (number 1-9) and we choose free position.
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():  # This function returns a boolean True if player wants to play again otherwise False.
    return input('Do you want to play again? (Yes or No)').lower().startswith('y')


# Here starts the main game logic ↓
print('Welcome to Tic Tac Toe!')
while True:
    TheBoard = [' '] * 10  # resets the board each game
    player1_marker, player2_marker = player_input()  # asks player 1 if he wants to be X or O
    turn = choose_first()  # randomly chooses who will start first (player 1 or player 2)
    print(turn + ' starts first')
    game_on = True

    while game_on:  # we stay in this nested while loop until game is win or draw
        display_board(TheBoard)

        if turn == 'Player 1':
            position = player_choice(TheBoard)  # This checks if player 1 chosen position is free on the board
            place_marker(TheBoard, player1_marker, position)  # Assigns player's position on the board

            if win_check(TheBoard, player1_marker):  # Checks for winning
                display_board(TheBoard)
                print('Player 1 you win the game!')
                game_on = False  # Breaks nested loop

            else:
                if full_board_check(TheBoard):  # Checks for a draw
                    display_board(TheBoard)
                    print('It is a draw!')
                    break  # Breaks nested loop

                else:  # If there is no win or draw, the game continues with the second player's turn.
                    turn = 'Player 2'  # then we go to the else statement ↓

        else:  # The same logic is used for player 2
            position = player_choice(TheBoard)
            place_marker(TheBoard, player2_marker, position)

            if win_check(TheBoard, player2_marker):
                display_board(TheBoard)
                print('Player 2 you win the game!')
                game_on = False

            else:
                if full_board_check(TheBoard):
                    display_board(TheBoard)
                    print('It is a draw!')
                    break

                else:
                    turn = 'Player 1'

    if not replay():  # if we don't want to play again this will break the main loop
        break
