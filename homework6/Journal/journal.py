# -*- coding: utf-8 -*-

"""
This module contains all the models we work with.
"""
__author__ = 'Anton Vodopyanov'

import pickle
import re

class Journal (object):
    def __init__(self, marks):
        self.marks = marks
        # self.school_class = school_class

    # creates a file if it not exist and write pupil's marks there
    def add_mark(self,marks):
        with open('journal.dat', 'wb') as file:
            pickle.dump(self.marks, file)

    # searches particular pupil marks
    def show_marks(self, name, last_name, school_class):
        try:
            with open('journal.dat', 'rb') as file:
                load = pickle.load(file)

        except:
            print('\nNope :(\n\n')

        external_loop_index = 0
        internal_loop_index = 0

        for list_element in load:
            match_count = 0
            for nested_element in list_element:
                if name == nested_element:
                    match_count += 1

                if last_name == nested_element:
                    match_count += 1

                if school_class == nested_element:
                    match_count += 1

            if match_count == 3:
                print(load[external_loop_index])
                
            else:
                internal_loop_index += 1

            external_loop_index += 1

    # loads all records from file
    def show_all_marks(self,):
        try:
            with open('journal.dat', 'rb') as file:
                load = pickle.load(file)
                print(load)
        except:
            print('\nNope :(\n\n')

    def load_info(self):
        try:
            with open('journal.dat', 'rb') as file:
                load = pickle.load(file)
                self.marks.extend(load)
        except:
            with open('journal.dat', 'wb') as file:
                print('The new journal has been created!\n')


    # input handling : will call a method depanding on user's input
    def input_parcer(self):

        string = input('\nPlease enter your command > ')
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
                self.marks.append(list(result))
                self.add_mark(self.marks)

            elif command[0][0] == 'show' and command[0][1] == 'all':
                self.show_all_marks()

            elif command[0][0] == 'show':

                name = command[0][1]
                last_name = command[0][2]
                school_class = command[0][3]

                self.show_marks(name,last_name,school_class)

                # search a string in file which will contain: name, last_name and school_class - > print it

        except:
            if string == 'exit' or string == 'quit':
                try:
                    raise KeyboardInterrupt
                except:
                    print("Bye!")
            else:
                print('Wrong input!')


def main():
    journal = Journal([])
    journal.load_info()

    while True:
        try:
            journal.input_parcer()
        except :
            print('\n\n*** Shutting down, bye! *** ')
            break
main()