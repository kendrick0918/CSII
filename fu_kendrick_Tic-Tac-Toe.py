
import random

def get_player_move(board, player, turn):
    '''
    Asks the player for row and column coordinates to place their piece.
    keeps asking until a valid answer is given
 
    Args:
        board (list): 2D list representing the current game board.
        player (str): Name of the player whose turn it is.
        turn (str): Current turn symbol, either ' x' or ' o'. (spaces for UI purposes)
 
    Returns:
        row (int): Row index (0-2) of the player's move.
        column (int): Column index (0-2) of the player's move.
 
    Raises:
        None
    '''

    while True:
        try:
            print(f"\nPlayer {player}'s turn. (_ means board space is empty)")
            row = int(input("Enter row 1-3")) -1
            column = int(input("Enter Column 1-3")) -1

            if row in range(3) and column in range(3):
                if board[row][column] == " _":
                    return row,column
                
                    # board[row-1][column-1] == turn
                    # return turn
                
                else: 
                    print("the cell is already taken")
            else:
                print("Invalid input, please choose a number within the range.")
            
        except ValueError:
            print("Invalid input, please enter a number ")
# get_player_move(board, player, turn): This function will get the player's move and return
def check_winner(board):
    '''
    Checks all 8 possible winning combinations to see if either player has won.
 
    Args:
        board (list): 2D list representing the current game board.
 
    Returns:
        str: ' x' if x wins, ' o' if o wins, None if no winner yet.
 
    Raises:
        None
    '''
# check_winner(board): This function will check if there is a winner and return the winner if there is one.
    if board [0][0] == ' x' and board [0][1] == ' x' and board [0][2] == ' x':
        return ' x'
    elif board [0][0] == ' x' and board [0][1] == ' x' and board [0][2] == ' x':
        return ' x'
    elif board [1][0] == ' x' and board [1][1] == ' x' and board [1][2] == ' x':
        return ' x'
    elif board [2][0] == ' x' and board [2][1] == ' x' and board [2][2] == ' x':
        return ' x'
    elif board [0][0] == ' x' and board [1][0] == ' x' and board [2][0] == ' x':
        return ' x'
    elif board [0][1] == ' x' and board [1][1] == ' x' and board [2][1] == ' x':
        return ' x'
    elif board [0][2] == ' x' and board [1][2] == ' x' and board [2][2] == ' x':
        return ' x'
    elif board [0][0] == ' x' and board [1][1] == ' x' and board [2][2] == ' x':
        return ' x'
    elif board [2][0] == ' x' and board [1][1] == ' x' and board [0][2] == ' x':
        return ' x'
    elif board [0][0] == ' o' and board [0][1] == ' o' and board [0][2] == ' o':
        return ' o'
    elif board [0][0] == ' o' and board [0][1] == ' o' and board [0][2] == ' o':
        return ' o'
    elif board [1][0] == ' o' and board [1][1] == ' o' and board [1][2] == ' o':
        return ' o'
    elif board [2][0] == ' o' and board [2][1] == ' o' and board [2][2] == ' o':
        return ' o'
    elif board [0][0] == ' o' and board [1][0] == ' o' and board [2][0] == ' o':
        return ' o'
    elif board [0][1] == ' o' and board [1][1] == ' o' and board [2][1] == ' o':
        return ' o'
    elif board [0][2] == ' o' and board [1][2] == ' o' and board [2][2] == ' o':
        return ' o'
    elif board [0][0] == ' o' and board [1][1] == ' o' and board [2][2] == ' o':
        return ' o'
    elif board [2][0] == ' o' and board [1][1] == ' o' and board [0][2] == ' o':
        return ' o'
    return None
def ai(board): 
    #making a smart ai
    # all combinations wins can be
    # ai(board): This function will make a random move for the computer
    #wins is all possible combinations to win the function. 
    '''
    Makes a smart move for the computer. First checks if the player is about to win
    and blocks them. If no threat is found, picks a random empty spot.
 
    Args:
        board (list): 2D list representing the current game board.
 
    Returns:
        None
 
    Raises:
        None
    '''
    wins = [
        [0,0, 0,1, 0,2],
        [1,0, 1,1, 1,2],
        [2,0, 2,1, 2,2],
        [0,0, 1,0, 2,0],
        [0,1, 1,1, 2,1],
        [0,2, 1,2, 2,2],
        [0,0, 1,1, 2,2],
        [2,0, 1,1, 0,2]
        ]
    for r1,c1,r2,c2,r3,c3 in wins: #
        line = [board[r1][c1], board[r2][c2], board[r3][c3]]
        if line.count(' x') == 2 and line.count(' _') == 1:   # player has two, block the empty one
            if board[r1][c1] == ' _':
                board[r1][c1] = ' o'
            elif board[r2][c2] == ' _':
                board[r2][c2] = ' o'
            else:
                board[r3][c3] = ' o'
            return
        
    while True:                 #this ony happens when the situation above is not true, kind of like a fallback option
        random_column = random.randint(0,2)
        random_row = random.randint(0,2)
        if board[random_column][random_row] == ' _':
            board[random_column][random_row] = " o"
            break
        else:
            continue

def is_draw(board):
    '''
    Checks if the board is completely full with no empty spaces left.
 
    Args:
        board (list): 2D list representing the current game board.
 
    Returns:
        bool: True if the board is full and it is a draw, False if there are still empty spaces.
 
    Raises:
        None
    '''
    # is_draw(board): This function will check if the board is full and return True if it is, and False if it isn't.
    for row in board:
        for cell in row:
            if cell == " _":
                return False
    return True

def display_board(board):
    '''
    Prints the tictactoe board
 
    Args:
        board (list): 2D list representing the current game board.
 
    Returns:
        None
 
    Raises:
        None
    '''
    # display_board(board): This function displays the tictactoe board to the user
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
            

def main():

    player = input("what is your name?")
    gamemode = input("Do you want to play against the Computer or another player? (1 for Ai, 2 for Multiplayer)") #user input for game
    if gamemode == "2":
        player2 = input("Player 2, what is your name?")


    while True:
        board = [[" _"," _"," _"], #this is my board
                    [" _"," _"," _"],
                    [" _"," _"," _"]]
        display_board(board)
        turn = 'x'
        while True:
            row,col = get_player_move(board, player, turn) 
            board[row][col] = ' x'
            display_board(board)

            winner = check_winner(board) #check winner after the User inputs
            if winner:
                print(winner, "wins!")
                break
            if is_draw(board):
                print("Game is a draw")
                break
            
            if gamemode == "2":
                print(f"{player2}'s move. (_ means board space is empty)") 
                row, col = get_player_move(board, player2, turn) #possible issues - resolved
                board[row][col] = ' o'
            else:
                print("ai move:")
                ai(board)
            display_board(board)
            
            winner = check_winner(board) #check winner after the Ai inputs
            if winner:
                print(winner, "wins")
                break
            if is_draw(board):
                print("Game is a draw")
                break

        playagain = input("Do you want to play again? (yes or no)") #playagain function
        if playagain == "yes":
            continue
        else:
            print("Thank you for playing, goodbye")
            break
main()