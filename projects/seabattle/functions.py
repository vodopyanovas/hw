# -*- coding: utf-8 -*-

"""
Main file. Contains program execution logic.
"""
__author__ = 'Anton Vodopyanov'

import os

from models import (
    Ship,
    Field,
)

def create_ships(field):   
    # creating ships objects where x1 - mean 1-deck, x2 - two decks and so on
    x1 = Ship(1,4,[])
    x2 = Ship(2,3,[])
    x3 = Ship(3,2,[])
    x4= Ship(4,1,[])
    # player_ships - list of all player's ships on a field
    player_ships = []
    # x1+x2+x3+x4 => means types of ships
    ships_to_place = 4

    question = ['Place one-deck ship', 'Place two-deck ship', 'Place three-deck ship', 'Place four-deck ship']

    # check if ships been already placed
    x1_flag = False
    x2_flag = False
    x3_flag = False
    x4_flag = False


    while ships_to_place > 0:
        print('Select what kind of ships do you want to place now:\n')
        for index, string in enumerate(question):
            print(index, string + '\n')
        
        usr_choice = input('> ')
        usr_choice = int(usr_choice)
        os.system('cls' if os.name == 'nt' else 'clear')
        Field.print_field(Field,player_ships)

        if usr_choice == 0:
            if x1_flag == False:
                x1.place_ship(player_ships)
                player_ships.extend(x1.coordinates)
                x1_flag = True
                ships_to_place -= 1
            else:
                print('\aError: This ships have been already added!\n\n')

        elif usr_choice == 1:
            if x2_flag == False:
                x2.place_ship(player_ships)
                player_ships.extend(x2.coordinates)
                x2_flag = True
                ships_to_place -= 1
            else:
                print('\aError: This ships have been already added!\n\n')
        
        elif usr_choice == 2:
            if x3_flag == False:
                x3.place_ship(player_ships)
                player_ships.extend(x3.coordinates)
                x3_flag = True
                ships_to_place -= 1
            else:
                print('\aError: This ships have been already added!\n\n')
        
        elif usr_choice == 3:
            if x4_flag == False:
                x4.place_ship(player_ships)
                player_ships.extend(x4.coordinates)
                x4_flag = True
                ships_to_place -= 1
            else:
                print('\aError: This ships have been already added!\n\n')

        else:
            print('\aError: Wrong input!\n\n')

    print('Great job! You\'ve just added all your ships!')        

    return player_ships