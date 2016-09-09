# -*- coding: utf-8 -*-
__author__ =    "Vodopyanov Anton"

import sys
from datetime import datetime

questions = ['Какой тип данных у чисел с плавающей точкой в Python?','Какую систему контроля версий мы используем?',
'Какой язык программирования мы изучаем?','Функция определения размера строки?','Команда вывода текста на экран?',
'Какое значение будет у переменной x, после выполения операции x=5//2 (в Python 3,5)?',
'Как называется переменная, областью видимости которой является весь модуль программы?']
answers = ['float','git','python','len','print','2','global']

log = open('log.txt', 'a')

name = input ('Привет! Это небольшая викторина по пройденной теме. Для начала игры введи своё имя \n> ')
now = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
log.write('######################################################################\n')
log.write(now + ' ' + name + '\n')

print ('\n{}, ответы указываются в виде одного слова/цифры/ на английском языке\n'.format(name))

# старт игры
run_game = 1
while run_game == 1:
    question_num = 0
    right_answers = 0
    while question_num < len(questions):
        print (questions[question_num])    
        usr_answer = input ('> ') 
        usr_answer = usr_answer.lower()
        now = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")	
        log.write(now + ' ' + usr_answer + '\n')
        
        # проверка ответов
        if usr_answer == answers[question_num]: 
            right_answers += 1        
            print ('\nВерно!') 
            print ('Количество правильных ответов: {}\n'.format(right_answers))

        else:
	        print ('Неверно.')
	        print ('Количество правильных ответов: {}\n'.format(right_answers))

        question_num += 1        
    # конец игры, подведение результатов
    run_game = 0 
    print ('\n{0}, за игру вы дали правильных ответов: {1} из {2}'.format(name, right_answers,len(questions)))
    now = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    log.write('\n')	
    log.write(now + ' Right answers: ' + str(right_answers) + ' of 7\n')
    log.write('______________________________________________________________________\n')
    
    gameover = input ('Для повторения игры нажмите 1, для выхода - 0 \n > ')
    if gameover == '1':
    	now = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    	log.write(now + ' ***New game*** \n')
    	run_game = 1
    elif gameover == '0':
        print ('\nСпасибо за игру!')
        log.close()
        break
    else:
    	print ('Нормально же попросил, ну! Не буду с тобой играть!')
    	log.close()
    



