import pickle as pkl
from sys import exit, stderr

try:
	with open('model.bin', 'rb+') as file:
		model = pkl.load(file)
except:
	print('model.bin doesn\'t exist!', file=stderr)
	exit(1)

while True:
	print('Enter x and y: ', end='')
	try:
		x, y = map(int, input().split())
		f = model.predict([[x, y]])[0]
		print(f'{x} + {y} = {round(f)}')
	except:
		exit(0)
