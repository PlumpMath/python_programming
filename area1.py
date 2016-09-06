from math import pi, sqrt
from area2 import area

def area_square(r):
	"""Return the area of a square with side length r."""
	assert r > o, 'r must be positive'
	return r * r
	

def area_circle(r):
	"""Return the area of a circle with radius r."""
	assert r > 0, 'r must be positive'
	return r * r * pi

def area_hexagon(r):
	"""Return the area of a regular hexagon with side length r."""
	assert r > 0, 'r must be positive'
	return r * r * 3 * sqrt(3) / 2
