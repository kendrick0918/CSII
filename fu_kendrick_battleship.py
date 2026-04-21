# Battleship
# Kendrick Fu | Date
import random
'''
fu_kendrick_battleship.py

Description: This code is battleship game where the user plays against the computer.

Features: 5 by 5 board, 5 ships placed randomly on the board, user interface include displays of the players board and computers board
          there are hidden boards storing the computer and player's ship locations.

Log: 1.2

Bugs: There is an issue with the code at the naming of the boards, the error says that it doesn't have a name/value to pull from so something is not formated/labeled correctly.
Bugs: still havent implemented a YOU WIN! at the end, or done a play again
'''
#Data
#arguments
#
def display_board(board):
    '''
    Prints the board/displays the board 

    Args:
        board(list): A list that represents the board that is being displayed
        
    Returns:
        none

    Raises:
        none in version 1.2
    '''

    # display the board with a label
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


def place_ships(board, num_dots):
    '''
    randomly places ships to the hidden board (the secret board that holds the where the ships are) as * symbols.

    Args:
        board(list): list represetning hidden baord to place ships on
        numdots(int): number of ships that is placed on the board
    Returns:
        none 

    Raises:
        no errors in this current version 1.2
    '''

    dots_placed = 0
    while dots_placed < num_dots:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] == " _":
            board[row][col] = " *"
            dots_placed += 1


def get_player_shot(display_board_computer):
    '''
    Asks the player for row and column coordinates to shoot at, keeps asking until a spot is avaiable (if coordinate is unshot).  

    Args:
        display_board_computer(list): List of the computer's display board, basically checking if the spot was shot already
    
    Returns:
        row(int): Row 0-4 (remeber 0 counts as a row) of the players shot
        col(int): Column 0-4 of the player shot (same as row for 0-4)

    Raises:
        valueerror has some errors, but it seems to be fixed 1.2
    '''

    # ask the user for coordinates to shoot at
    while True:
        try:
            row = int(input("Enter row (1-5): ")) - 1
            col = int(input("Enter column (1-5): ")) - 1
            if row in range(5) and col in range(5):
                if display_board_computer[row][col] == " H" or display_board_computer[row][col] == " M":
                    print("You already shot there! Try again.")
                else:
                    return row, col
            else:
                print("Invalid input, please choose a number within the range.")
        except ValueError:
            print("Invalid input, please enter a number.")


def check_shot(display, hidden, row, col):
    '''
    Def here. 

    Args:
        display(list): list of display board to mark Hit (H) or Miss (M) on. 
        hidden(list): list of the hidden board to check for ships
        row(int): Row 0-4 (remeber 0 counts as a row) of the players shot
        col(int): Column 0-4 of the player shot (same as row for 0-4)
    
    Returns:
        hit(bool): True if the shot hit a ship, false if it missed 

    Raises:
        none version 1.2
    '''

    # check if the shot hit or missed, update display and hidden boards
    if hidden[row][col] == " *":
        display[row][col] = " H"
        hidden[row][col] = " H"
        return True
    else:
        display[row][col] = " M"
        return False


def computer_shot(display_board_player, hidden_board_player):
    '''
    Randomly selects a coordinate for the computer to shoot at on the player's board, but if spot is shot at already, it keeps going until there is an unshot spot

    Args:
        display_board_player (list): 2D list of the players display board
        hidden_board_player(list): 2D list of the player's hidden board 
    
    Returns:
        row(int): Row 0-4 (remeber 0 counts as a row) of the players shot
        col(int): Column 0-4 of the player shot (same as row for 0-4)

    Raises:
        none version 1.2
    '''

    # computer randomly shoots at the player's board
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if display_board_player[row][col] != " H" and display_board_player[row][col] != " M":
            return row, col


def check_all_sunk(hidden):
    '''
    Def here. 

    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 
    '''

    # check if all ships have been hit
    for row in hidden:
        for cell in row:
            if cell == " *":
                return False
    return True


def main():
    player = input("What is your name? ")
    num_dots = int(input("How many ships do you want? (1-5): "))
    print(f"\nWelcome to Battleship, {player}!")
    print(f"There are {num_dots} ships hidden on each board.")
    print("First to sink all the opponent's ships wins!")
    print("H = Hit, M = Miss, _ = Unknown\n")

    while True:
        display_board_player = [[" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"]]

        hidden_board_player =  [[" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"],
                                [" _"," _"," _"," _"," _"]]

        display_board_computer = [[" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"]]

        hidden_board_computer =  [[" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"],
                                  [" _"," _"," _"," _"," _"]]

        place_ships(hidden_board_player, num_dots)
        place_ships(hidden_board_computer, num_dots)

        while True:
            print("Computer's Board")
            display_board(display_board_computer)
            print(player,"'s Board")
            display_board(display_board_player)

            # player shoots at computer
            print(f"\n{player}, where do you want to shoot?")
            row, col = get_player_shot(display_board_computer)
            hit = check_shot(display_board_computer, hidden_board_computer, row, col)
            if hit:
                print("hit!")
            else:
                print("missed")

            if check_all_sunk(hidden_board_computer):
                display_board(display_board_computer, f"{player}'s shots:")
                print(f"\nYou sunk all the computer's ships! You win, {player}!")
                break

            # computer shoots at player
            row, col = computer_shot(display_board_player, hidden_board_player)
            hit = check_shot(display_board_player, hidden_board_player, row, col)
            if hit:
                print(f"Computer hit your ship! Position of your ship is: row {row+1}, column {col+1}!")
            else:
                print(f"Computer missed! Row {row+1}, Column {col+1}.")

            if check_all_sunk(hidden_board_player):
                display_board(display_board_player, "Computer's shots:")
                print(f"\nThe computer sunk all your ships, you lose.")
                break

        playagain = input("\nDo you want to play again? (yes or no) ")
        if playagain == "yes":
            continue
        else:
            print("Thank you for playing")
            break


main()