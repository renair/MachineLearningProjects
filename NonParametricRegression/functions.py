import cores
import math
import matplotlib.pyplot as plt
import numpy as np

def get_coeficients(arr, x, h, window):
	return np.array(list(map(lambda xi : window(x, xi, h), arr)))

def get_used(coefs, values):
	return list(map(lambda x: x[1], filter(lambda x: x[0] > 0, zip(coefs, values))))

def previous_processing(coefs, values, processing_coeff = 2):
	used = get_used(coefs, values)
	to_remove = []
	for x in used:
		vals = used.copy()
		vals.remove(x)
		mean = np.mean(vals)
		if abs(x/mean) > processing_coeff:
			to_remove.append(x)
	for i in range(len(coefs)):
		coefs[i] = 0 if values[i] in to_remove else coefs[i]

def predict_value(testX, testY, x, h, window = cores.square_core):
	coefs = get_coeficients(testX, x, h, window)
	previous_processing(coefs, testY, 7)
	values = np.multiply.reduce([testY, coefs])
	top = np.add.reduce(values)
	bottom = np.add.reduce(coefs)
	return top/bottom

def calculate_loss(testX, expectedY, resultY):
	deviation = np.subtract.reduce([expectedY, resultY])
	deviation_squares = [x**2 for x in deviation]
	return np.add.reduce(deviation_squares)

def run_test(testX, function, selectedH, windowFunction, drawPlot = False):
	testY = [function(x) for x in testX]
	testY[3] = 100
	testY[14] = 100
	testY[40] = 100
	testY[80] = 100
	resultY = [predict_value(testX, testY, x, selectedH, window=windowFunction) for x in testX]
	print("Loss in test: " + str(calculate_loss(testX, testY, resultY)))
	if drawPlot:
		plt.plot(testX, testY, '-g', label='Original data')
		plt.plot(testX, resultY, 'ob', label='Result data')
		plt.legend()
		plt.show()

def train_h(testX, function, startH, windowFunction, required_loss = 1):
	selectedH = startH
	testY = [function(x) for x in testX]
	current_loss = required_loss + 1
	while current_loss > required_loss:
		resultY = [predict_value(testX, testY, x, selectedH, window=windowFunction) for x in testX]
		current_loss = calculate_loss(testX, testY, resultY)
		print("Loss is: " + str(current_loss))
		if current_loss > 0:
			selectedH /= 2
	return selectedH * 2