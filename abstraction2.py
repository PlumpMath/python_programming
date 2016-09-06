#Usage
def makeRational(n, d):
    return pair(n, d)

def mulRational(x, y):
    """Violate abstraction by using other than constructor and selectors"""
    return pair(getitem_pair(x,0) * getitem_pair(y,0), getitem_pair(x,1) * getitem_pair(y,1))

def addRational(x, y):
    """Violate abstraction by using other than constructor and selectors"""
    nx, dx = getitem_pair(x,0), getitem_pair(x,1)
    ny, dy = getitem_pair(y,0), getitem_pair(y,1)
    return pair(nx * dy + ny * dx, dx * dy)

def eqRational(x, y):
    """Violate abstraction by using other than constructor and selectors"""
    return getitem_pair(x,0) * getitem_pair(y,1) == getitem_pair(y,0) * getitem_pair(x,1)

def toString(x):
    """Violate abstraction by using other than constructor and selectors"""
    return '{0}/{1}'.format(getitem_pair(x,0), getitem_pair(x,1))


#Representation
#Representation is provided by constructors and selectors using higher order functions

#Constructor 
def pair(x, y):
    from fractions import gcd
    g = gcd(x, y)
    """Return a functional pair"""
    def dispatch(m):  
        if m == 0:
            return x // g
        			
        elif m == 1:
            return y // g
    return dispatch

#Selector
def getitem_pair(p, i):
    """Return the element at index of pair p"""
    return p(i)   			