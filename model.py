import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sys import exit, stderr
import pickle as pkl

try:
	dataset = pd.read_csv('data.csv')
except:
	print('data.csv not found!', file=stderr)
	exit(1)

X = dataset[['x', 'y']].values
Y = dataset['f'].values

model = LinearRegression()
model.fit(X, Y)

with open('model.bin', 'wb+') as file:
	pkl.dump(model, file)
