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
	print('\ndiffs plus - вкл/выкл примеры с плюсом.')
	print('diffs minus - вкл/выкл примеры с минусом.')
	print('Чтобы продолжить решать примеры напишите 1')

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

		if(command == 'continue' or command == '1'):
			rand = ['plus', 'minus']
			if(choice(rand) == 'plus'):
				commandplus()
			else:
				commandminus()

except Exception as a:
	print(str(a))

os.system('pause')
