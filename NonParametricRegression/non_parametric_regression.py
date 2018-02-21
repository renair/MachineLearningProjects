import math
import cores
import numpy as np
import matplotlib.pyplot as plt
import functions as fns

def train_function1(x):
	return math.exp(x)*math.sin(x**2)

def train_function2(x):
	return math.log(x)

def train_function3(x, A = 0.4, B = 0.4):
	return A*x+ B

datasetX = np.arange(0.0000001, 2, 0.025)
datasetY = [train_function1(x) for x in datasetX]
testH = 0.1
window = cores.triangle_core

#def train_h(testX, function, startH, windowFunction)
print("Square core:")
fns.train_h(datasetX, train_function1, 0.1, cores.square_core)
fns.train_h(datasetX, train_function2, 0.1, cores.square_core)
fns.train_h(datasetX, train_function3, 0.1, cores.square_core)

print("\nTriangle core:")
fns.train_h(datasetX, train_function1, 0.1, cores.triangle_core)
fns.train_h(datasetX, train_function2, 0.1, cores.triangle_core)
fns.train_h(datasetX, train_function3, 0.1, cores.triangle_core)

print("\nBisquare core:")
fns.train_h(datasetX, train_function1, 0.1, cores.bisquare_core)
fns.train_h(datasetX, train_function2, 0.1, cores.bisquare_core)
fns.train_h(datasetX, train_function3, 0.1, cores.bisquare_core)

print("\nGausian core:")
fns.train_h(datasetX, train_function1, 0.1, cores.gaussian_core, drawPlot = False)
fns.train_h(datasetX, train_function2, 0.1, cores.gaussian_core, drawPlot = False)
fns.train_h(datasetX, train_function3, 0.1, cores.gaussian_core, drawPlot = False)

#resultY = [fns.predict_value(datasetX, datasetY, x, testH, window=window) for x in datasetX]
#print(fns.calculate_loss(datasetX, datasetY, resultY))

#plt.plot(datasetX, datasetY, '-g', label='Original data')
#plt.plot(datasetX, resultY, 'ob', label='Result data')
#plt.legend()
#plt.show()
