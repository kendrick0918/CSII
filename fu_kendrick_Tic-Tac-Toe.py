# Tic-Tac-Toe
# Kendrick Fu | 4/2/26
import random

# remember that all the spacing is for board ui and is important for the game to work properly, so when you are checking for winners, make sure to include the space before the x and o.
# The board is a 2d list, and the user will input the row and column they want to place their piece in. The game will check for a winner after each move, and if there is a winner, it will end the game. If there is no winner and the board is full, it will declare a draw. The user can choose to play against another player or against the computer. The computer will make random moves.







#all formating for this function needs to be reviewed if referencing, all has to align.
def get_player_move(board, player, turn):
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
        
    while True:                 #this ony happens when the situation above is not true, kindof like a fallback option
        random_column = random.randint(0,2)
        random_row = random.randint(0,2)
        if board[random_column][random_row] == ' _':
            board[random_column][random_row] = " o"
            break
        else:
            continue

def is_draw(board):
    # is_draw(board): This function will check if the board is full and return True if it is, and False if it isn't.
    for row in board:
        for cell in row:
            if cell == " _":
                return False
    return True

def display_board(board):
    # display_board(board): This function will display the board to the user.
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
            

def main():

#problems you might run into: 

    
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
                row, col = get_player_move(board, player2, turn) #possible issues
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