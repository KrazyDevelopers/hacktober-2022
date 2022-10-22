# importing random to generate random positions for system's turn
import random
import sys

# from main_multi_player import play_tic_tac_toe


one = "Player1"
two = "player2"
def single_player():
    one = "Player1"

    def start_game():  # defining starting of game
        global one
        display_board()
        one = input("hey user please enter your name here : ")
        show_positions()
        user_input()

    block = ['_', '_', '_',
             "_", '_', '_',
             "_", '_', '_']

    def display_board():  # display_board()
        print(block[0] + "|" + block[1] + "|" + block[2])
        print(block[3] + "|" + block[4] + "|" + block[5])
        print(block[6] + "|" + block[7] + "|" + block[8])

    # display_board()  # calling function to show grid
    block_positions = ['_1', '_2', '_3',
                       '_4', '_5', '_6',
                       '_7', '_8', '_9']

    def show_positions():  # showing the positions for refernce
        print(block_positions[0] + "|" + block_positions[1] + "|" + block_positions[2])
        print(block_positions[3] + "|" + block_positions[4] + "|" + block_positions[5])
        print(block_positions[6] + "|" + block_positions[7] + "|" + block_positions[8])

    def user_input():  # function for user input
        global one
        print("Choose a position")
        pos = int(input("Enter the position choosen:(1-9) "+ one +" 's turn"))
        if check_validity(pos):  # checking validity of input value
            if block[pos - 1] != "X" and block[pos - 1] != "O":  # adjusting with index values of list
                block[pos - 1] = "X"

                if check_for_winner("X"):  # checking for winner
                    display_board()
                    print("Player 1 :" + one + " has won!! the game😁 👍")
                    end_game()
                # ### if check_if_tie(): ####

                elif check_tie() == 5:
                    print("Its a tie")
                    end_game()
                else:
                    pc_input()
            else:
                print("Place occupied already ,choose some other position")
                print("Try again:::")
                user_again_input()

                pc_input()  # flipping turn to pc
        else:
            print("Re-enter value,its invalid")
            user_input()

    # system's turn

    def pc_input():  # pc input
        pc = random.randint(1, 9)

        if block[pc - 1] != "X" and block[pc - 1] != "O":
            block[pc - 1] = "O"
            print(display_board())  # displaying changed grid
            if check_for_winner("O"):  # checking for winner
                print("YOU LOSE 😮, the system has won")
                end_game()

            else:
                user_input()
                return 
        else:
            pc_input()  # flipping turn to user

    def user_again_input():  # if user tries to use preoccupied position
        pos = int(input("your choice:"))
        if block[pos - 1] != "X" and block[pos - 1] != "Y":
            block[pos - 1] = "X"
            pc_input()

        else:  # if invalid input then again calling the function
            print("Place occupied already ,choose some other position")
            user_again_input()

    def check_for_winner(symbol):# function to check for winner in every possible way 
                                    
        if block[0] == block[1] == block[2] == symbol:     # (8 ways)
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

    def check_tie():
        count = 0
        for i in block:
            if i == "X":
                count += 1
        return count

    def end_game():
        
        print("game Over")
        sys.exit()

    # calling start function
    try:
        start_game()
    except:
        print()
