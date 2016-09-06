from operator import mul

def square(x):
    print('In square with value: ' + str(x))
    return mul(x, x)

def repeat1(f, n):
    def identity(x):
        return x
    def apply_n_times(x):
        print('In apply_n_times with: ' + str(n))
        return repeat1(f,n-1)(f(x))
    if n < 0:
        raise ValueError("Cannot apply a function %d times" % (n))
    elif n == 0:
        return identity
    else:
        return apply_n_times


def repeat2(f, n, x):
    if n < 0:
        raise ValueError("Cannot apply a function %d times" % (n))
    elif n == 0:
        return x
    else:
        return repeat2(f, n-1, f(x))	
g = repeat2(square, 2, 5)

print(g)