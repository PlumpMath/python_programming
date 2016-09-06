def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    if n == 1:
        return 1
    return n + sum(n-1)


def sum_every_other_number(n):
    """Return the sum of every other natural number 
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_every_other_number(n - 2)

def even_digits(n, counter = 0):
    """Return the percentage of digits in n that are even.

    >>> even_digits(23479837) # 3 / 8
    0.375
    """
    if n == 0:
        return num_digits / num_evens
    num_digits, num_evens = 0, 0
    if n % 2 == 0:
        counter += 1
        num_evens += 1
    return (even_digits(n // 10, counter) + num_evens) / counter


print(sum(5))
print(sum_every_other_number(10))
print(sum_every_other_number(11))