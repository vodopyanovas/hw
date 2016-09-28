# -*- coding: utf-8 -*-

"""
This module contains all the models we work with.
"""
__author__ = 'Anton Vodopyanov'

import os
#from functions import handle_wasd

# will use this class for storing some information
# class Storage(object):
#     __obj = None

#     players = None

#     @classmethod
#     def __new__(cls, *args):
#         if cls.__obj is None:
#             cls.__obj = object.__new__(cls)
#             cls.items = []
#         return cls.__obj

# describes player
class Player(object):

    def __init__(self, name, turn):
        self.name = name
        self.turn = turn


# class creates game field and prints it
class Field (object):    

    def __init__(self, name):
        self.name = name 

    def print_field(self, ships):

        def update_field(ships):
            #cache_list = []
            n = 0
            print('\n')
            for i in ships:    
                print('{row:>2}'.format(row=str(i)), end = ' ')
                n += 1
                #cache_list.append(str(i))
                if n == 10:
                    n = 0
                    print('\n')
                    # print('\t\t', end ='')                        
                    # for x in cache_list:                       
                    #     print('{row:>2}'.format(row=str(x)), end = ' ')
                    #     n += 1                    
                    #     if n == 10:                        
                    #         print('\n')                        
                    #         n = 0  
                    #         cache_list.clear()              
        
        ship = '[]'
        field = []        
        [field.append(i) for i in range(100)]
        #[cells2.append(i) for i in range(self.FIELD_RANGE)] - список выстрелов и попаданий
        
        for x in ships:
            field.pop(x)
            field.insert(x,ship)

            # field.pop(x+9)
            # field.insert(x+9,'\'')            
            # field.pop(x-9)
            # field.insert(x-9,'\'')
            
            # field.pop(x+11)
            # field.insert(x+11,'\'')            
            # field.pop(x-11)
            # field.insert(x-11,'\'')

        update_field(field)

# describes ship structure, gets coordinates for placing ships on a game field
class Ship (object):
    
    def __init__(self, decks, count,coordinates):
        self.decks = decks
        self.count = count
        self.coordinates = coordinates

    def place_ship(self,player_ships):

        # getting direction  
        def get_direction(head, body):
            head = int(head)
            body = int(body)
            if body == head - 10:
                return 'up'
            elif body == head + 10:
                return 'down'
            elif body == head - 1:
                return 'left'
            elif body == head + 1:
                return 'right'
            else:
                return False                      

        # check for "Out of borders"
        def check_borders(cell,direction):           

            if cell in (9,19,29,39,49,59,69,79,89,99) and direction == 'left':
                print('You can\'t place ship left')
                while cell in (9,19,29,39,49,59,69,79,89,99):
                    cell = input('Out of borders! Try one more time> ')
                    cell = int(cell)                    
                return cell

            elif cell in (0,10,20,30,40,50,60,70,80,90) and direction == 'right':
                print('You can\'t place ship right')
                while cell in (0,10,20,30,40,50,60,70,80,90):
                    cell = input('Out of borders! Try one more time> ')
                    cell = int(cell)                    
                return cell

            elif cell > 99 or cell < 0:
                while  cell > 99 or cell < 0:
                    cell = input('Out of borders! Try one more time> ')
                    cell = int(cell) 
                return cell    

            return cell

        # checking uniqueness of inputed values    
        def check_uniqueness(cell, coordinates):
            cell = int(cell)
            
            if cell in coordinates:
                while cell in coordinates:
                    print('Try to place your ship somewhere else. There is a ship here.')
                    cell = input('Where should we place a ship?\n> ')   
                    cell = int(cell)
            return cell

            # options = {'right':cell+1, 'left':cell-1, 'down':cell+10, 'up':cell-10} - пока не надо
       
        # getting coordinates of ships
        def get_coorginates(self,player_ships):

            decks_to_place = self.decks

            if decks_to_place > 1:                         
                place_head = input('\nWhere should we place head of a {}-deck ship?\n> '.format(self.decks))
                check = check_uniqueness(place_head,player_ships)
                check2 = check_borders(check, None)
                player_ships.append(int(check2))
                os.system('cls' if os.name == 'nt' else 'clear')
                Field.print_field(Field, player_ships)

                decks_to_place -= 1

                # дальше задаём координаты окружения корабля - place +-9, 11 - пока не нужно

                while decks_to_place >= 1:
                    place = input('\nWhere should we place next part of a {}-deck ship?\n> '.format(self.decks)) 
                    
                    # checking for correct input and placement
                    direction = get_direction(place_head, place)
                    if direction != False:                    
                        check1 = check_uniqueness(place,player_ships)
                        check2 = check_borders(check1, direction)
                        player_ships.append(int(check2))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        Field.print_field(Field, player_ships)
                        place_head = check2
                        decks_to_place -= 1

                    else :
                        print('Wrong place! You can\'t place ship here')                        
                    
                    # в зависимости от направления дозабиваем окружение - пока не нужно                                   
                
            else:
                place = input('Where should we place a {}-deck ship?\n> '.format(self.decks)) 
                check = check_uniqueness(place,player_ships)
                check2 = check_borders(check, None)
                player_ships.append(int(check2))
                os.system('cls' if os.name == 'nt' else 'clear')
                Field.print_field(Field, player_ships)

            print('{}-deck ship has been added'.format(self.decks))
            return self.coordinates

        if self.count > 1:
            ship = get_coorginates(self,player_ships)
            print('Left to add: {} ships\n'.format(self.count-1))

            while self.count > 1:                
                ship=get_coorginates(self,player_ships)
                self.count -=1
                print('Left to add: {} ships\n'.format(self.count-1))
            return ship
            
        else:
            ship = get_coorginates(self,player_ships)
            return ship
            
# will contain game logic 
class Shot (object):
    
    def __init__(self, ships, shots):
        self.ships = ships        
        self.shots = shots

    def make_shoot(self, field):

        def mark_shot(shot_index,shot_result):
            field.pop(shot_index)
            field.insert(shot_index,shot_result)

        def get_aim():  

            aim = input('Where should we shoot sir?\n> ')
            aim = int(aim)
            while aim in self.shots:
                    print('We\'ve already shooted there! Let\'s choose another place to fire sir!')
                    aim = input('Where to shoot?\n> ')  
                    aim = int(aim)              
            self.shots.append(aim)
            return aim

        aim = get_aim()

        if aim in self.ships:

            mark_shot(self.shots[-1],shot_result = '*')                         
            while aim in self.ships:
                mark_shot(self.shots[-1],shot_result = '*') 
                print('Hit!')
                print('Try to kill him now!')   
                aim = get_aim()
            mark_shot(self.shots[-1],shot_result = '~')
            print('Off target!')    
        else:           
            mark_shot(self.shots[-1],shot_result = '~')
            print('Off target!')
        return field