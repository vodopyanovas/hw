# -*- coding: utf-8 -*-

"""
Main file. Contains program execution logic.
"""
__author__ = 'Anton Vodopyanov'

import os
import random

from functions import create_ships

from models import (
    Player,
    Field,
    Ship,
    Shot,)

# finds who will play first
def get_turn(player1, player2):
    players =[player1, player2]
    for x in range(1000):
        i=random.randrange(2)
    first_turn = players[i]
    first_turn.turn = 0
    return first_turn

# condition of end of the game
def game_over():
    pass
# main function
def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nHello my friend! Let\'s play a game!')
    field = Field('new')


    print('So, to play a game you need to call your friend and say me your names!\n')
    p1_name = input('Tell me the name of the first player: ')
    p2_name = input('Tell me the name of the second player: ')
    player1 = Player(p1_name,1)
    player2 = Player(p2_name,1)

    os.system('cls' if os.name == 'nt' else 'clear')
    # turn = get_turn(player1,player2)

    print('\nNow it\'s time to place your ships on a game field! And the first player will be {}\n'.format(player1.name))
    os.system('cls' if os.name == 'nt' else 'clear')
    #field.print_field('')
    p1_ships = create_ships(field)


    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nNow it\'s time to place its ships For the second player {}'.format(player2.name))
    input('\n\npress Enter to continue...')

    os.system('cls' if os.name == 'nt' else 'clear')
    field.print_field('')
    p2_ships = create_ships(field)

# LEFT TO DO
# Перед каждым выстрелом отрисовывается новое поле, с известными выстрелами, пустыми пространствами и уничтоженными кораблями
# • По очереди каждый игрок делает выстрел, если выстрел приходится в цель, то игрок продолжает стрелять.
# • Игра длится, пока все корабли одно из игроков не будут уничтожены







# temp text

# while True:
#     try:
#         command = parse_user_input()
#         perform_command(command)
#     except UserExitException:
#         break
#     except KeyboardInterrupt:
#         print('Shutting down, bye!')
#         break







if __name__ == '__main__':
    start_game()


# below there are test values, all
# field1 = Field('Player1')
# field2 = Field('Player2')
