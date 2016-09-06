from math import pi, sqrt

def area(r, shape_constant):
	"""Return the area of a shape from length r."""
	assert r > o, 'r must be positive'
	return r * r * shape_constant

def area_square(r):
	"""Return the area of a square with side length r."""
	return area(r, 1)

def area_circle(r):
	"""Return the area of a circle with radius r."""
	return area(r, pi)

def area_hexagon(r):
	"""Return the area of a regular hexagon with side length r."""
	return area(r, 3 * sqrt(3) / 2)

