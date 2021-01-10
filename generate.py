from random import randint

def f(x, y):
	return x + y

with open('data.csv', 'w+') as file:
	file.write(f'x,y,f\n')
	for i in range(10000):
		x = randint(1, 10)
		y = randint(1, 10)
		fxy = f(x, y)
		file.write(f'{x},{y},{fxy}\n')
