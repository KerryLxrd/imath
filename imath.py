# by https://vk.com/k3rry1xrd/

import os
from random import randint, choice

valueplus = 1
valueminus = 1

distance1 = 100
distance2 = 1000

expressions = ['Примеры с плюсом - включены!', 'Примеры с плюсом - выключены!', 'Примеры с минусом - включены!', 'Примеры с минусом - выключены!'] 

username = os.environ.get("USERNAME")

def diffs():
	if(valueplus == 1 and valueminus == 1):
		print('\n' + expressions[0])
		print(expressions[2])
	elif(valueplus == 1 and valueminus == 0):
		print('\n' + expressions[0])
		print(expressions[3])
	elif(valueplus == 0 and valueminus == 1):
		print('\n' + expressions[1])
		print(expressions[2])
	else:
		print('\n' + expressions[1])
		print(expressions[3])

def info():
	print('\n"info" - просмотр команд')
	print('"continue" - продолжить решение задач')
	print('"diffs" - просмотр включенных/выключенных задач')
	print('"diffs plus" - включение/выключение задач с плюсом')
	print('"diffs minus" - включение/выключение задач с минусом')
	print('"cls" - очистка программы от строк')
	print('"distance" - просмотр диапозона чисел в данный момент')
	print('"distance change" - редактирование значение диапозона')
 
def commandplus():
	a = randint(distance1, distance2)
	b = randint(distance1, distance2)
	if(valueplus == 1):
		result = a + b
		print(str(a) + ' + '+ str(b))
		answer = input('>')
		while answer != result:
			if(str(answer) == 'ответ'):
				print('\nОтвет - ' + str(result))	
				break
			if(int(answer) == result):
				print('\nПравильно! Ответ - ' + str(result))
				break
			else:
				print('Не правильно! Чтобы посмотреть ответ напишите \"ответ\"')		
				answer = input('>')
	else:
		commandminus()

def commandminus():
	a = randint(distance1, distance2)
	b = randint(distance1, distance2)
	if(valueminus == 1):
		result = a - b
		print(str(a) + ' - '+ str(b))
		answer = input('>')
		while answer != result:
			if(str(answer) == 'ответ'):
				print('\nОтвет - ' + str(result))	
				break
			if(int(answer) == result):
				print('\nПравильно! Ответ - ' + str(result))
				break
			else:
				print('\nНе правильно! Чтобы посмотреть ответ напишите \"ответ\"\n')		
				answer = input('>')
	else:
		commandplus()

info()

def distance():
	global distance1, distance2
	distance1 = int(input('1: '))
	distance2 = int(input('2: '))
	print('Ваш диапозон чисел теперь с ' + str(distance1) + ' по ' + str(distance2))

try:
	while True:
		print('')
		command = input(username + '>')

		if(command == 'diffs plus' and valueplus == 0):
			valueplus = 1
			print('\n' + expressions[0] + '\n')
		elif(command == 'diffs plus' and valueplus == 1):
			valueplus = 0
			print('\n' + expressions[1] + '\n')

		if(command == 'diffs minus' and valueminus == 0):
			valueminus = 1
			print('\n' + expressions[2] + '')
		elif(command == 'diffs minus' and valueminus == 1):
			valueminus = 0
			print('\n' + expressions[3] + '')		

		if(command == 'diffs'):
			diffs()

		if(command == 'info'):
			info()

		if(command == 'cls' or command == 'clear'):
			os.system('cls')

		if(command == 'distance change'):
			distance()

		if(command == 'distance'):
			print('Ваш диапозон чисел в данный момент с ' + str(distance1) + ' по ' + str(distance2))

		if(command == 'continue' or command == '1'):
			rand = ['plus', 'minus']
			if(choice(rand) == 'plus'):
				commandplus()
			else:
				commandminus()

except Exception as a:
	print(str(a))

os.system('pause')
