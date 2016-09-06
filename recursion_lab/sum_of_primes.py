def sum_primes_up_to(n):
    if n == 1:
        return 1
    elif is_prime(n):
        return n + sum_primes_up_to(n-1)
    else:
        return sum_primes_up_to(n - 1)

def is_prime(n):
    for m in range(2, n//2):
        if not n % m:
            return False
    return True