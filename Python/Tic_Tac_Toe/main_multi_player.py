# importing file main_single_player that has complete program for single player game
from main_single_player import *
import sys


def multi_player():
    one = "player1"
    two = "player2"

    def start_game():  # defining starting of game
        global one
        global two
        display_board()
        one = input("Enter your name player 1 ")
        two = input("Enter your name player 2 ")
        show_positions()
        player_1()

    block = ['_', '_', '_',
             '_', '_', '_',  # structure of 3X3 grid
             '_', '_', '_']

    def display_board():
        print(block[0] + "|" + block[1] + "|" + block[2])  # displaying the matrix
        print(block[3] + "|" + block[4] + "|" + block[5])
        print(block[6] + "|" + block[7] + "|" + block[8])

    block_positions = ['_1', '_2', '_3',
                       '_4', '_5', '_6',
                       '_7', '_8', '_9']

    def show_positions():  # showing the positions for refernce
        print(block_positions[0] + "|" + block_positions[1] + "|" + block_positions[2])
        print(block_positions[3] + "|" + block_positions[4] + "|" + block_positions[5])
        print(block_positions[6] + "|" + block_positions[7] + "|" + block_positions[8])

    def player_1():  # user input

        global one
        print()
        pos = int(input("Choose a position(1-9): " + one + "'s turn "))
        if check_validity(pos):  # checking validity of input value

            if block[pos - 1] != "X" and block[pos - 1] != "O":  # adjusting with index values of list
                block[pos - 1] = "X"

                display_board()  # displaying changed grid

                if check_for_winner("X") is True:  # checking for winner
                    print("Player 1 :" + one + " has won!! 😁 👍")
                    end_game()
                elif check_tie() == 5:  # if its a tie
                    print("Its a tie")
                    end_game()
                else:
                    player_2()  # flipping turn to player_2


            else:  # checking if entered position is not preoccupied
                print("Place occupied already ,choose some other position")
                print("Try again::::")
                display_board()
                player_1()
        else:  # if invalid input then again calling the function
            print("Re-enter value,its invalid")
            player_1()

    def player_2():  # every thing similar for second player but with slight
        global two  # variations that are necessary
        print()
        pos = int(input("Choose a position(1-9): " + two + "'s turn "))
        if check_validity(pos):
            if block[pos - 1] != "X" and block[pos - 1] != "O":
                block[pos - 1] = "O"
                display_board()

                if check_for_winner("O") is True:
                    print("Player 2 " + two + "has won 👌 😁")
                    end_game()
                elif check_tie() == 5:  # if its a tie
                    print("Its a tie")
                    end_game()
                else:
                    player_1()  # flipping players again
            else:
                print("Place occupied already ,choose some other position")
                print("Try again::::")
                display_board()
                player_2()
        else:
            print("Re-enter value,its invalid")
            player_2()

    def check_for_winner(symbol):  # function to check for winner in every possible way (8 ways)

        if block[0] == block[1] == block[2] == symbol:
            return True
        elif block[0] == block[3] == block[6] == symbol:
            return True
        elif block[0] == block[4] == block[8] == symbol:
            return True

        elif block[2] == block[5] == block[8] == symbol:
            return True
        elif block[6] == block[7] == block[8] == symbol:
            return True

        elif block[3] == block[4] == block[5] == symbol:
            return True
        elif block[1] == block[4] == block[7] == symbol:
            return True
        elif block[2] == block[4] == block[6] == symbol:
            return True
        else:
            return False

    def check_validity(num):  # defining validity function for input

        if num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True

        else:
            return False

    def check_tie():  # defining check_tie()
        count = 0
        for i in block:
            if i == "X":
                count += 1
        return count

    def end_game():  # defining end function
        print("game Over")

        play_again = str(input("do you want to play again?(yes or no): "))
        if play_again == 'yes':
            return play_tic_tac_toe()
        elif play_again != 'yes' and play_again != 'no':
            print("please answer in yer/no")
        else:
            print("Good Bye..Nice time with u 😄")
            sys.exit()

    # calling start function
    try:
        start_game()
    except:
        print()


def play_tic_tac_toe():  # selection between single player and multiplayer
    print("do you want to play :")
    print("Single Player(s): or Multi Player(m): ")
    play = str(input("'s' or 'm' ??? ", ))
    if play == 's':
        return single_player()
    elif play == 'm':
        return multi_player()
    else:
        print("choose between 's' and 'm' !")
        return play_tic_tac_toe()


# wanna play tic tac toe game::?? 😋
play_tic_tac_toe()
