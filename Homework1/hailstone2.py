def hailstone(n):
    """Print the terms of the 'hailstone sequence' from n to 1, and
    return the length of the sequence."""
    assert n > 0
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + hailstone(n // 2)
        else:
            return 1 + hailstone((n * 3) + 1)

if __name__ == '__main__':
    result = hailstone(10)
    print("number of iterations:", result)