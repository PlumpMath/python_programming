#Use
def makeRational(n, d):
    return Rational(n, d)

def mulRational(x, y):
    """Violate abstraction by using other than constructor and selectors"""
    return Rational(getNumer(x)*getNumer(y), getDenom(x)*getDenom(y)) #x and y are abstract data

def addRational(x, y):
    """Violate abstraction by using other than constructor and selectors"""
    nx, dx = getNumer(x), getDenom(x)
    ny, dy = getNumer(y), getDenom(y)
    return Rational(nx * dy + ny * dx, dx * dy)

def eqRational(x, y):
    """Violate abstraction by using other than constructor and selectors"""
    return getNumer(x) * getDenom(y) == getNumer(y) * getDenom(x)

def toString(x):
    """Violate abstraction by using other than constructor and selectors"""
    return '{0}/{1}'.format(getNumer(x), getDenom(x))

#Representation
# Representation is provided by constructors and selectors using tuples

#Constructor
from fractions import gcd
def Rational(n, d):
    """Construct a rational number x that represents n/d."""
    g = gcd(n, d)
    return (n // g, d // g) #this is concrete representation of a rational number


#Selector
from operator import getitem
def getNumer(x):
    """Return the numerator of rational number x."""
    return getitem(x, 0)

#Selector
def getDenom(x):
    """Return the denominator of rational number x."""
    return getitem(x, 1)