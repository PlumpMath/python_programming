def sum_of_digits(n):
    if n < 10:
        return n
    else:
        remainder, quotient = n % 10, n // 10
        return remainder + sum_of_digits(quotient)

print(sum_of_digits(12345))

		