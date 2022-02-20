import random

""" vvvv YOUR CODE STARTS HERE vvvv """


class Player:
    # constructor

    # validity_check

    # __repr__

    pass


class Game:
    # constructor

    # validity_check

    # run_game

    # get_results

    # __repr__

    pass


def rock_paper_scissors(number_of_rounds, player_a, player_b):

    # create player_a

    # create player_b

    # create game

    # run game

    # get result

    """ ^^^^ YOUR CODE ENDS HERE ^^^^ """
    return result


if __name__ == '__main__':

    N = 1000
    PLAYER_A = {
        "paper": 0.8,
        "scissors": 0.1,
        "rock": 0.1,
    }
    PLAYER_B = {
        "paper": 0.1,
        "scissors": 0.8,
        "rock": 0.1,
    }
    rock_paper_scissors(N, PLAYER_A, PLAYER_B)
    # Approximate output: {'player_a': 170, 'player_b': 640, 'tie': 190} (could vary slightly because of the randomness)

    # Test case 2
    N = 100
    PLAYER_A = {
        "paper": 0,
        "scissors": 1,
        "rock": 0,
    }
    PLAYER_B = {
        "paper": 0,
        "scissors": 0,
        "rock": 1,
    }
    assert rock_paper_scissors(N, PLAYER_A, PLAYER_B) == {'player_a': 0, 'player_b': 100, 'tie': 0}

    # Test case 3
    N = 0
    PLAYER_A = {
        "paper": 0,
        "scissors": 1,
        "rock": 0,
    }
    PLAYER_B = {
        "paper": 0,
        "scissors": 0,
        "rock": 1,
    }
    assert rock_paper_scissors(N, PLAYER_A, PLAYER_B) is False
