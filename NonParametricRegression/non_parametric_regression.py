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

datasetX = np.arange(0.0000001, 4, 0.025)
datasetY = [train_function1(x) for x in datasetX]
datasetY[3] = 100
datasetY[15] = -100
testH = 0.1
window = cores.triangle_core

#def run_test(testX, function, startH, windowFunction, drawPlot = False)
#print("Square core:")
#fns.run_test(datasetX, train_function1, 0.1, cores.square_core)
#fns.run_test(datasetX, train_function2, 0.1, cores.square_core)
#fns.run_test(datasetX, train_function3, 0.1, cores.square_core)
#
#print("\nTriangle core:")
#fns.run_test(datasetX, train_function1, 0.1, cores.triangle_core)
#fns.run_test(datasetX, train_function2, 0.1, cores.triangle_core)
#fns.run_test(datasetX, train_function3, 0.1, cores.triangle_core)
#
#print("\nBisquare core:")
#fns.run_test(datasetX, train_function1, 0.1, cores.bisquare_core)
#fns.run_test(datasetX, train_function2, 0.1, cores.bisquare_core)
#fns.run_test(datasetX, train_function3, 0.1, cores.bisquare_core)
#
#print("\nGausian core:")
#fns.run_test(datasetX, train_function1, 0.1, cores.gaussian_core, drawPlot = False)
#fns.run_test(datasetX, train_function2, 0.1, cores.gaussian_core, drawPlot = False)
#fns.run_test(datasetX, train_function3, 0.1, cores.gaussian_core, drawPlot = False)

h = 0.08
#h = fns.train_h(datasetX, train_function1, h, cores.triangle_core)
fns.run_test(datasetX, train_function2, h, cores.triangle_core, drawPlot = True)
print(h)
