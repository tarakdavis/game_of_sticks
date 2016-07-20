import sys

def get_stick_count():
    print("Welcome to the game of sticks! You will need 2 players to play this game. \n Your objective is to NOT be the player with only 1 stick left.\n Let's get started!")
    stick_count = input("How many sticks do you want to start with? Choose a number between 10-100: ")
    return stick_count

def initial_stick_count(stick_count):
    try:
        if int(stick_count) <= 100 and int(stick_count) >= 10:
            #return True
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
    if initial_stick_count:
        board = initial_stick_count(get_stick_count())
    sticks_to_choose = "1, 2, 3"
    while True:
        player1_choice = input("Player 1: Choose a number from {}: ".format(sticks_to_choose))
        board -= int(player1_choice)
        print("There are {} sticks left.".format(board))
        if is_game_over(board):
            if board == 1:
                print("Player 1: You win!")
                break
            elif board == 0:
                print("Player 2: You win!")
                break
        player2_choice = input("Player 2: Choose a number from {}: ".format(sticks_to_choose))
        board -= int(player2_choice)
        print(("There are {} sticks left.".format(board)))
        if is_game_over(board):
            if board == 1:
                print("Player 2: You win!")
                break
            elif board == 0:
                print("Player 1: You win!")
                break
    play_again = input("Would you like to play again? Y/n: ")
    if play_again.lower() == 'n':
        print("Thanks for playing!")
        sys.exit()
    else:
        main()


if __name__ == '__main__':
    main()
#ai
# #hat = {1:(1,2,3), 2:(1,2,3), 3:(1,2,3), 4:(1,2,3), 5:(1,2,3), 6:(1,2,3), 7:(1,2,3),
#         8:(1,2,3), 9:(1,2,3), 10:(1,2,3), 11:(1,2,3), 12:(1,2,3), 13:(1,2,3), 14:(1,2,3),
#         15:(1,2,3), 16:(1,2,3), 17:(1,2,3), 18:(1,2,3), 19:(1,2,3), 20:(1,2,3), 21:(1,2,3),
#         22:(1,2,3), 23:(1,2,3), 24:(1,2,3), 25:(1,2,3), 26:(1,2,3), 27:(1,2,3), 28:(1,2,3),
#         29:(1,2,3), 30:(1,2,3), 31:(1,2,3), 32:(1,2,3), 33:(1,2,3), 34:(1,2,3), 35:(1,2,3),
#         36:(1,2,3), 37:(1,2,3), 38:(1,2,3), 39:(1,2,3), 40:(1,2,3), 41:(1,2,3), 42:(1,2,3),
#         43:(1,2,3), 44:(1,2,3), 45:(1,2,3), 46:(1,2,3), 47:(1,2,3), 48:(1,2,3), 49:(1,2,3),
#         50:(1,2,3), 51:(1,2,3), 52:(1,2,3), 53:(1,2,3), 54:(1,2,3), 55:(1,2,3), 56:(1,2,3),
#         57:(1,2,3), 58:(1,2,3), 59:(1,2,3), 60:(1,2,3), 61:(1,2,3), 62:(1,2,3), 63:(1,2,3),
#         64:(1,2,3), 65:(1,2,3), 66:(1,2,3), 67:(1,2,3), 68:(1,2,3), 69:(1,2,3), 70:(1,2,3),
#         71:(1,2,3), 72:(1,2,3), 73:(1,2,3), 74:(1,2,3), 75:(1,2,3), 76:(1,2,3), 77:(1,2,3),
#         78:(1,2,3), 79:(1,2,3), 80:(1,2,3), 81:(1,2,3), 82:(1,2,3), 83:(1,2,3), 84:(1,2,3),
#         85:(1,2,3), 86:(1,2,3), 87:(1,2,3), 88:(1,2,3), 89:(1,2,3), 90:(1,2,3), 91:(1,2,3),
#         92:(1,2,3), 93:(1,2,3), 94:(1,2,3), 95:(1,2,3), 96:(1,2,3), 97:(1,2,3), 98:(1,2,3),
#         99:(1,2,3), 100:(1,2,3)}
