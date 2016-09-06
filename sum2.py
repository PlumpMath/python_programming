def identity(k):
	return k

def cube(k):
	return pow(k, 3)

def summation1(n, term):
    if n == 0:
        return 0
    else:
        return term(n) + summation(n-1, term)

def summation2(n, term):
    def sum_with_closure(n, accum):
        if(n == 0):
            return accum
        else:
            return sum_with_closure(n - 1, accum + term(n)) 		
    return sum_with_closure(n, 0)

def sum_naturals(n):
	return summation2(n, identity)

def sum_cubes(n):
	return summation2(n, cube)

if __name__ == '__main__':
    sum = sum_naturals(4)
    print(sum)