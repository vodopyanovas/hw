# -*- coding: utf-8 -*-

"""
This module contains all the commands we work with.
If you want to create a new command it should be placed here.
"""

from __future__ import print_function

import sys
import inspect
#import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import (
    BaseItem,
    ToDoItem,
    ToBuyItem,
    ToReadItem,
    Storage,
)
from utils import get_input_function

__author__ = 'sobolevn'
__author__ = 'Anton Vodopyanov'


class BaseCommand(object):
    """
    Main class for all the commands.
    Defines basic method and values for all of them.
    Should be subclassed to create new commands.
    """

    @staticmethod
    def label():
        """
        This method is called to get the commands short name:
        like `new` or `list`.
        """
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        """
        This method is called to run the command's logic.
        """
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        #Dynamic load:
        def class_filter(klass):
            return inspect.isclass(klass) \
            and klass.__module__ == BaseItem.__module__ \
            and issubclass(klass, BaseItem) \
            and klass is not BaseItem
    
        classes = inspect.getmembers(
        sys.modules[BaseItem.__module__],
        class_filter,
        )
        # classes = {
        #     'ToDoItem': ToDoItem,
        #     'ToBuyItem': ToBuyItem,
        #     'ToReadItem' : ToReadItem
        #     }
        return dict(classes)

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                selected_key = list(classes.keys())[selection]
                selected_class = classes[selected_key]
                print('Selected: {}'.format(selected_class.__name__))
                print()

                new_object = selected_class.construct()

                objects.append(new_object)
                print('Added {}'.format(str(new_object)))
                print()
                return new_object
                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Are you a blind?')


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')


class DoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):  
        
        objects_list = [obj for obj in objects if obj.done == False]         

        if len(objects_list) == 0:
            print('There are no undone items.')
            return 
        else:            
            for index, obj in enumerate(objects_list):
                if obj.done == False:                    
                    print('{}: {}'.format(index, str(obj)))                                         

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number to mark done: '))
                selected_key = objects_list[selection]        
                selected_key.done = True
                print(selected_key)
                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Are you a blind?')


class UndoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'undone'

    def perform(self, objects, *args, **kwargs):  
        
        objects_list = [obj for obj in objects if obj.done == True]         

        if len(objects_list) == 0:
            print('There are no done items.')
            return 
        else:            
            for index, obj in enumerate(objects_list):
                if obj.done == True:                    
                    print('{}: {}'.format(index, str(obj)))                                         

        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number to mark undone: '))
                selected_key = objects_list[selection]        
                selected_key.done = False
                print(selected_key)
                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Are you a blind?')
        


class SaveCommand(BaseCommand):
    @staticmethod
    def label():
        return 'save'    


    def perform(self, objects, *args, **kwargs): 
        for index, obj in enumerate(objects):
            file = open('ToDoList.txt','a')
            if len(objects) == 0:
                print('There are no items in storage.')
                break
            else:
                save = str(obj)
                #json.dump(save, f)
                file.write(save +'\n')            
            file.close()


    def result_return(self,array, item, row):        
        row=int(row)
        check = array[item][0][0][0][row]
        heading = array[item][0][1][0][row]
        if item == 1:
            price = array[item][0][2][0][row]            
            return check,heading,price
        elif item == 2:
            writer = array[item][0][2][0][row]            
            return check, heading, writer
        else:
            return check, heading


    def file_parcer(self):
        file = open('ToDoList.txt','r', encoding = 'utf8')
        
        def flag_checker(line):
            flag_check = line[:1]
            if flag_check == '+':
                check = True
            else:
                check = False
            return check

        ToDo_list, ToDo_done, ToDo_heading = [],[],[]    
        ToBuy_list, ToBuy_done, ToBuy_heading, ToBuy_price = [],[],[],[]
        ToRead_list, ToRead_done, ToRead_heading, ToRead_writer = [],[],[],[]
        

        for line in file:        

            if 'ToDo' in line:
                ToDo_done.append(flag_checker(line))
                ToDo_heading.append(line[2::].rstrip().split(': ')[1])
                x = [[ToDo_done],[ToDo_heading]]
                if x not in ToDo_list:
                    ToDo_list.append(x)
                
                
            if 'ToBuy' in line:
                ToBuy_done.append(flag_checker(line))
                x = line[2::].rstrip().split(': ')[1].split(' for ')
                ToBuy_heading.append(x[0])
                ToBuy_price.append(x[1])
                x = [[ToBuy_done],[ToBuy_heading], [ToBuy_price]] 
                if x not in ToBuy_list:
                    ToBuy_list.append(x)            
                        
                
            if 'ToRead' in line:
                ToRead_done.append(flag_checker(line))
                x = line[2::].rstrip().split(': ')[1].split(' written by ')
                ToRead_heading.append(x[0])
                ToRead_writer.append(x[1])
                x = [[ToRead_done],[ToRead_heading], [ToRead_writer]]
                if x not in ToRead_list:
                    ToRead_list.append(x)
                
        file.close()
        return ToDo_list, ToBuy_list, ToRead_list                        
 

    def load_items(self,*args): 
        # save array from file to read_file
        read_file = self.file_parcer()

        # add object ToDo from file
        for i in range(len(read_file[0][0][0][0])):
            new_object_Do = ToDoItem()
            a=self.result_return(self,read_file, 0,i)
            new_object_Do.done = a[0]
            new_object_Do.heading = a[1]
            objects.append(new_object_Do)

        # add object ToBuy from file
        for i in range(len(read_file[1][0][0][0])):
            new_object_Buy = ToBuyItem()
            a=self.result_return(self,read_file, 1,i)
            new_object_Buy.done = a[0]
            new_object_Buy.heading = a[1]
            new_object_Buy.price = a[2]
            objects.append(new_object_Buy)

        # add object ToRead from file
        for i in range(len(read_file[2][0][0][0])):
            new_object_Read = ToReadItem()
            a=self.result_return(self,read_file, 2,i)
            new_object_Read.done = a[0]
            new_object_Read.heading = a[1]
            new_object_Read.writer = a[2]
            objects.append(new_object_Read)           