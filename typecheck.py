from math import sqrt
def isnumber(thing):
    try:
	    int(thing)
    except:
        return False
    return True


def make_safe(f, isnumber):
    def type_check(datum):
        if isnumber(datum):
            return f(datum)
        else:
            return False
    return type_check

	
safe_sqrt = make_safe(sqrt, isnumber)
print(safe_sqrt('123'))
