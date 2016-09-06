def approx_eq_1(x, y, tolerance=1e-10):
    return abs(x - y) <= tolerance

def approx_eq_2(x, y, tolerance=1e-7):
    return abs(x - y) <= abs(x) * tolerance

def approx_eq(x, y):
    if x == y:
	    return True
    return approx_eq_1(x, y) or approx_eq_2(x, y)