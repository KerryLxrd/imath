# by https://vk.com/k3rry1xrd/

import os, time
from random import randint, choice

valueplus = 1
valueminus = 1

distance1 = 10
distance2 = 100

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
	print('"distance" - просмотр диапозона чисел в данный момент')
	print('"distance change" - редактирование значение диапозона')
	print('"cls" - очистка программы от строк')

def commandplus():
	a = randint(distance1, distance2)
	b = randint(distance1, distance2)
	if(valueplus == 1):
		result = a + b
		print(str(a) + ' + '+ str(b))
		start_time = time.time()
		answer = input('>')
		while answer != result:
			if(str(answer) == 'ответ'):
				print('\nОтвет - ' + str(result))
				break
			if(int(answer) == result):
				print('\nПравильно! Ответ - ' + str(result))
				print('Время: ' + str(int((time.time() - start_time))) + ' сек.')
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
		start_time = time.time()
		answer = input('>')
		while answer != result:
			if(str(answer) == 'ответ'):
				print('\nОтвет - ' + str(result))
				break
			if(int(answer) == result):
				print('\nПравильно! Ответ - ' + str(result))
				print('Время: ' + str(int((time.time() - start_time))) + ' сек.')
				break
			else:
				print('\nНе правильно! Чтобы посмотреть ответ напишите \"ответ\"\n')		
				answer = input('>')
	else:
		commandplus()

info()

def distance():
	global distance1, distance2
	distance1 = int(input('Первое число в диапозоне: '))
	distance2 = int(input('Второе число в диапозоне: '))
	print('Ваш диапозон чисел теперь с ' + str(distance1) + ' по ' + str(distance2))

try:
	while True:
		print('')
		command = input('imath\\' + username + '>')
		if(command == 'diffs plus' and valueplus == 0):
			valueplus = 1
			print('\n' + expressions[0] + '\n')
		elif(command == 'diffs plus' and valueplus == 1):
			valueplus = 0
			print('\n' + expressions[1] + '\n')
		elif(command == 'diffs minus' and valueminus == 0):
			valueminus = 1
			print('\n' + expressions[2] + '')
		elif(command == 'diffs minus' and valueminus == 1):
			valueminus = 0
			print('\n' + expressions[3] + '')		
		elif(command == 'diffs'):
			diffs()
		elif(command == 'info'):
			info()
		elif(command == 'cls' or command == 'clear'):
			os.system('cls')
		elif(command == 'distance change'):
			distance()
		elif(command == 'distance'):
			print('Ваш диапозон чисел в данный момент с ' + str(distance1) + ' по ' + str(distance2))
		elif(command == 'continue' or command == '1'):
			rand = ['plus', 'minus']
			if(choice(rand) == 'plus'):
				commandplus()
			else:
				commandminus()
		else:
			print('"' + command + '" не является внутренней или внешней командой, исполняемой программой')
except Exception as a:
	print(str(a))

os.system('pause')
