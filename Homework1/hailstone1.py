def hailstone(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + hailstone(n // 2)
    else:
        return [n] + hailstone(3 * n + 1)
		

if __name__ == '__main__':
    sequence = hailstone(10)
	""" I/O is used here to just verify the results in driver code"""
	print(sequence)
	
    