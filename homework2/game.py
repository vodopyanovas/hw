# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# `msvcrt` module is used for handling user's input
# https://docs.python.org/3/library/msvcrt.html
import msvcrt


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'X'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.    
    """
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]
    shuffle = random.sample(l,len(l))    
    return shuffle


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    n = 0
    print('\n')
    for i in field:    
        print('{row:>3}'.format(row=str(i)), end = ' ')
        n += 1
        if n == 4:
            print('\n')
            n = 0
    return None


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    pass


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    while True:
        key = ord(msvcrt.getch())
        k=chr(key)
        if k in MOVES.keys():
            return str((MOVES[k]))
        else:
            print('Use only w,a,s,d buttons for moving')


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    l = shuffle_field()


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
    
    
    