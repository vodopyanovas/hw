# -*- coding: utf-8 -*-
__author__ =    "Vodopyanov Anton"

import sys

right_answers = 0
usr_answer = input ('Какой тип данных у чисел с плавающей точкой в Python? \n > ')
usr_answer = usr_answer.lower()

if usr_answer == 'float':
    right_answers +=1
    print ('Верно!') # \n Количество правильных ответов: {}'.format(right_answers))
    print ('Количество правильных ответов: {}'.format(right_answers))
    
else:
	print ('Неверно')




