from game_of_sticks import *


def test_how_many_sticks_to_start():
    player_choice_1 = '48'
    player_choice_2 = '0'
    player_choice_3 = '102'
    player_choice_4 = 'k'

    assert initial_stick_count(player_choice_1) == True
    assert initial_stick_count(player_choice_2) == False
    assert initial_stick_count(player_choice_3) == False
    assert initial_stick_count(player_choice_4) == False

def test_is_game_over():
    board_1 = 3
    board_2 = 1
    board_3 = 0

    assert is_game_over(board_1) == False
    assert is_game_over(board_2) == True
    assert is_game_over(board_3) == True

#def test_is_game_over():
