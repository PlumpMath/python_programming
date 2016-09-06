def squareroot(a):
    x = 1
    def apply(x):
        if x*x == a:
            return x
        else:
            return apply((x + a/x)/2)
    return apply(x)

result = squareroot(2)
print(result)


	
	
	