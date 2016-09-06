def make_derivative(f, h=1e-5):
    """Returns a function that is the derivative of f.
       	
    >>> def f(x):
            return x*x
    >>> square = f
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3)
    6.0   	   
    """
    def derivative(a):
        return (f(a+h) - f(a))/h
    return derivative
