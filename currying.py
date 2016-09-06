def curry(f):
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g

from operator import add
make_adder = curry(add)
make_adder(2)(3)