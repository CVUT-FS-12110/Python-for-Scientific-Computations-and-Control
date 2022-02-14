# imported functions
from math import sqrt, asin, pi

""" vvvv SPACE FOR YOUR OWN FUNCTIONS vvvv """




""" ^^^^ SPACE FOR YOUR OWN FUNCTIONS ^^^^ """


# Predefined function - don't change the header
def circles(circle_1, circle_2):
    """ vvvv YOUR CODE STARTS HERE vvvv """



    """ ^^^^ YOUR CODE ENDS HERE ^^^^ """
    return message_out, overlap_out  # Predefined function return - don't change it


if __name__ == '__main__':
    # asserts for testing of your function
    assert circles((0, 0, 5), (0, 10, 5)) == ('Outer contact', 0)
    assert circles((0, 0, 3), (1.5, 1.5, 0.8)) == ('Absorbed circle', 2.0106192982974678)
    assert circles((0, 0, 4), (2, 0, 2)) == ('Inner contact', 12.566370614359172)
    assert circles((0, 0, 5), (100, 100, 10)) == ('Separated circles', 0)
    assert circles((0, 0, 4.5), (10, 10, 15)) == ('Circle intersection', 37.47580042619734)
    assert circles((-10.25, -20.5, 4), (-10.25, -20.5, 4)) == ('Identical circles', 50.26548245743669)
