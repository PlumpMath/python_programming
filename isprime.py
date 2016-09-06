def is_prime(n):
    def f(n, k):
        if k > (n // 2):
            return True
        elif n % k == 0:
            return False
        else:
            return f(n, k + 1)
    return f(n, 2)


def nth_prime(n):
    def traverse_for_nth_prime(count, k):
        if count == n:
           return k-1
        elif is_prime(k):
            return traverse_for_nth_prime(count + 1, k + 1)
        else:
            return traverse_for_nth_prime(count, k + 1)
    return traverse_for_nth_prime(0, 2)


print(nth_prime(20))