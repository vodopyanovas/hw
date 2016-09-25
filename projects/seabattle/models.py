#from functions import handle_wasd

# will use this class for storing some information
class Storage(object):
    __obj = None

    players = None

    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
            cls.items = []
        return cls.__obj

# describes player
class Player(object):
    def __init__(self, name, queue):
        self.name = name
        self.queue = queue

    def __str__(self):
        return self.name

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
        indexes = []        
        [indexes.append(i) for i in range(100)]
        #[cells2.append(i) for i in range(self.FIELD_RANGE)] - список выстрелов и попаданий
        
        for x in ships:
            indexes.pop(x)
            indexes.insert(x,ship)

            # indexes.pop(x+9)
            # indexes.insert(x+9,'\'')            
            # indexes.pop(x-9)
            # indexes.insert(x-9,'\'')
            
            # indexes.pop(x+11)
            # indexes.insert(x+11,'\'')            
            # indexes.pop(x-11)
            # indexes.insert(x-11,'\'')


        update_field(indexes)     



# describes ship structure, gets coordinates for placing ships on a game field
class Ship (object):
    
    def __init__(self, decks, count,coordinates):
        self.decks = decks
        self.count = count
        self.coordinates = coordinates        
        

    def place_ship(self,):  
        # getting direction to ...
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

        # checking uniqueness of inputed values    
        def check_row(cell, coordinates):
            cell = int(cell)
            while cell in coordinates:
                print('You can\'t place your ship here. Try to place your ship somewhere else')
                cell = input('Where should we place head of a ship?\n> ')   
                #cell = int(cell)
            return cell

        def get_coorginates(self):             
            decks_to_place = self.decks

            if decks_to_place > 1:                
                    
                place_head = input('Where should we place head of a {}-deck ship?\n> '.format(self.decks))              
                
                check = check_row(place_head,self.coordinates)                
                self.coordinates.append(int(check))
                # дальше задаём координаты окружения корабля - place +-9, 11

                while decks_to_place > 1:
                    place = input('Where should we next part of a {}-deck ship?\n> '.format(self.decks)) 

                    # проверка влезет/не влезет 
                   # direction = get_direction(place_head, place)                      
                    
                    check = check_row(place,self.coordinates) 
                    self.coordinates.append(int(check))
                    # в зависимости от направления дозабиваем окружение

                    decks_to_place -= 1                  
                
            else:        
                place = input('Where should we place a {}-deck ship?\n> '.format(self.decks)) 
                check = check_row(place,self.coordinates)             
                self.coordinates.append(int(check))  

            print('\n{}-deck ship has been added'.format(self.decks))
            return self.coordinates

             
        if self.count > 1:
            ship = get_coorginates(self)            
            print('Left to add: {} ships\n'.format(self.count-1))

            while self.count > 1:                
                ship=get_coorginates(self) 
                self.count -=1
                print('Left to add: {} ships\n'.format(self.count-1))                
            return ship
            
        else:
            ship = get_coorginates(self)
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


        


