import cores
import matplotlib.pyplot as plt
import numpy as np

def get_coeficients(arr, x, h, window):
	return np.array(list(map(lambda xi : window(x, xi, h), arr)))

def predict_value(testX, testY, x, h, window = cores.square_core):
	coefs = get_coeficients(testX, x, h, window)
	values = np.multiply.reduce([testY, coefs])
	top = np.add.reduce(values)
	bottom = np.add.reduce(coefs)
	return top/bottom

def calculate_loss(testX, expectedY, resultY):
	deviation = np.subtract.reduce([expectedY, resultY])
	deviation_squares = [x**2 for x in deviation]
	return np.add.reduce(deviation_squares)

def train_h(testX, function, startH, windowFunction, drawPlot = False):
	selectedH = startH
	testY = [function(x) for x in testX]
	resultY = [predict_value(testX, testY, x, selectedH, window=windowFunction) for x in testX]
	print(calculate_loss(testX, testY, resultY))
	if drawPlot:
		plt.plot(testX, testY, '-g', label='Original data')
		plt.plot(testX, resultY, 'ob', label='Result data')
		plt.legend()
		plt.show()
