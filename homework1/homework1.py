# -*- coding: utf-8 -*-
__author__ =    "Vodopyanov Anton"

import sys

name = input ('Привет! Это небольшая викторина по пройденной теме. Для начала игры введи своё имя \n> ')
print ('{}, ответы указываются в виде одного слова/цифры/символа'.format(name))

run_game = 1
while run_game == 1:
    #цикл while	
    right_answers = 0
    # начало цикла for 0-7
    usr_answer = input ('Какой тип данных у чисел с плавающей точкой в Python? \n > ') # вопрос берётся из файла 
    usr_answer = usr_answer.lower()

    if usr_answer == 'float': #ответ берётся из файла
        right_answers +=1
        print ('Верно!') # \n Количество правильных ответов: {}'.format(right_answers))
        print ('Количество правильных ответов: {}'.format(right_answers))
    
    else:
	    print ('Неверно')

    # конец цикла for

    run_game = 0 # пока хз
    print ('{0}, за игру вы дали {1} правильных ответов из 8'.format(name, right_answers))

    gameover = input ('Для повторения игры нажмите 1, для выхода - 0 \n > ')
    if gameover == '1':
    	run_game = 1
    elif gameover == '0':
        print ('Спасибо за игру!')
        break
    # конец цикла while



