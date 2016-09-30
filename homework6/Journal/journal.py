# -*- coding: utf-8 -*-

"""
This module contains all the models we work with.
"""
__author__ = 'Anton Vodopyanov'

import pickle
import re

class Journal (object):
    def __init__(self,):
        pass
        # self.school_class = school_class

    # creates a file if it not exist and write pupil's marks there
    def add_mark(self,result):

        with open('journal.dat', 'ab') as file:
            pickle.dump(result, file)

    # searches particular pupil marks
    def show_marks(self):
        pass

    # loads all records from file
    def show_all_marks(self,):
        try:
            with open('myfile.dat', 'rb') as file:
                for _ in file:
                    load = pickle.load(file)
                    print(load)
        except (EOFError):
            print('\nNope :(\n\n')

    # input handling : will call a method depanding on user's input
    def input_parcer(self):

        string = input('Please enter your command > ')
        regexp1 = re.findall(r'(show).*(all).*(marks)', string)
        regexp2 = re.findall(r"(add)\s(\w+)\s(\w+).*(\d\w).*(\d)\s\w+?\s(\w+)", string)
        regexp3 = re.findall(r"(show)\s(\w+)\s(\w+).*?(\d\w)\s?(\w+)", string)

        command = None

        if len(regexp1) > 0:
            command = regexp1

        elif len(regexp2) > 0:
            command = regexp2

        elif len(regexp3) > 0:
            command = regexp3

        try:
            if command[0][0] == 'add':
                result = command[0][1:]
                self.add_mark(result)

            elif command[0][0] == 'show' and command[0][1] == 'all':
                self.show_all_marks()

            elif command[0][0] == 'show':

                name = command[0][1]
                last_name = command[0][2]
                school_class = command[0][3]
                # search a string in file which will contain: name, last_name and school_class - > print it

        except:
            if string == 'exit' or string == 'quit':
                try:
                    raise KeyboardInterrupt
                except:
                    print("Bye!")
            else:
                print('Wrong input!')

b7 = Journal()
b7.input_parcer()
