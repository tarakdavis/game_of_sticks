import sys

def start_game():
    print("Welcome to the game of sticks! You will need 2 players to play this game. At any time press ENTER to leave the game.")
    stick_count = input("How many sticks do you want to start with? Choose a number between 10-100: ")
    return stick_count

def initial_stick_count(stick_count):
    try:
        if int(stick_count) <= 100 and int(stick_count) >= 10:
            return True
            return int(stick_count)
        elif int(stick_count) > 100 or int(stick_count) < 10:
            print("Please provide a number within the range of 10-100.")
            return False
    except ValueError:
        if stick_count.isalpha():
            print("Please enter a number.")
            return False
        else:
            print("Thanks for playing! Bye.")
            return False

def is_game_over(board):
    if board <= 1:
        return True
    else:
        return False

def main():
    start_game()
    if initial_stick_count:
        board = initial_stick_count(start_game())
    sticks_to_choose = "1, 2, 3"
    while True:
        player1_choice = input("Player 1: Choose a number from {}: ".format(sticks_to_choose))
        board -= int(player1_choice)
        print("There are {} sticks left.".format(board))
        if is_game_over(board):
            break
        player2_choice = input("Player 2: Choose a number from {}: ".format(sticks_to_choose))
        board -= int(player2_choice)
        print(("There are {} sticks left.".format(board)))
        if is_game_over(board):
            break
    play_again = input("Would you like to play again? Y/n: ")
    if play_again.lower() == 'n':
        print("Thanks for playing!")
        sys.exit()
    else:
        main()

        # players = ["Player 1", "Player 2"]
        # if players[0]:



#     while has_sticks_left:
#         if sticks_in_game.isalpha():
#             print("Please enter a number.")
#             continue
#         elif not sticks_in_game >= 1 and sticks_in_game <= 3:
#             print("Please provide a number within the range of 1-3.")
#             continue
#         elif sticks_in_game == "":
#             print("Thanks for playing! Bye.")
#             break
#
# def has_sticks_left(has_more_turns):
#     return initial_stick_count - sticks_in_game =
#

if __name__ == '__main__':
    main()
