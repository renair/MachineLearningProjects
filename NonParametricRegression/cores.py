import math

def object_distance(x1, x2):
	return abs(x1 - x2)

def get_r(x1, x2, h):
	return object_distance(x1,x2)/h

def square_core(x, xi, h):
	if get_r(x, xi, h) <= 1:
		return 1
	else:
		return 0

def triangle_core(x, xi, h):
	r = get_r(x, xi, h)
	if r <= 1:
		return 1 - r
	else:
		return 0

def bisquare_core(x, xi, h):
	r = get_r(x, xi, h)
	if r <= 1:
		return (1 - r**2)**2
	else:
		return 0

def gaussian_core(x, xi, h):
	r = get_r(x, xi, h)
	return math.exp(r**2)
