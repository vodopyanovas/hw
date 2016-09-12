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
    one of which is a empty space. -> print_field(field)  
    """
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]
    shuffle = random.sample(l,len(l))    
    return shuffle


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.  <- perform_move(field, key)
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
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,EMPTY_MARK]
    if field == l:
        print('You win!')
        return True

    else:
        return False 


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state. <- список с элементами
    :param key: move direction. <- handle_user_input()
    :return: new field state (after the move). -> print_field(field)
    :raises: IndexError if the move can't me done.
    """
    cant_left=[0,4,8,12]
    cant_right=[3,7,11,15]
    cant_up=[0,1,2,3]
    cant_down=[12,13,14,15]
    f1 = field
    f2 =[ ]
    index_x = f1.index('X')    
    delta = index_x+int(key)

    if index_x in cant_left and int(key)== -1:
        print('Can\'t move left\a')
        return f1
    elif index_x in cant_right and int(key)== 1:
        print('Can\'t move right\a')
        return f1
    elif index_x in cant_up and int(key)== -4:
        print('Can\'t move up\a')
        return f1
    elif index_x in cant_down and int(key)== 4:
        print('Can\'t move down\a')
        return f1
    else:
        f2=f1.copy()
        f2.pop(index_x)
        f2.insert(index_x, f1[delta])  
        f2.pop(delta)
        f2.insert(delta, f1[index_x])
        return f2


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move. -> perform_move(field, key)
    """
    while True:
        try:  
            key = ord(msvcrt.getch())
            k=chr(key)
            if k in MOVES.keys():
                return str((MOVES[k]))
        except KeyboardInterrupt:
            print('Shutting down!')
        else:
            print('Use only w,a,s,d buttons for moving. For exit the game press Ctrl+Break.')


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    print_field(field)
    while is_game_finished(field) == False:
        user_input = handle_user_input()
        move = perform_move(field, user_input)
        print_field(move)
        field = move



if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
    
    
    