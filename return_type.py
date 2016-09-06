import dis
def f(n):
    def g(k):
        return n + k
    return g

result = f(3)
print("f disclosure ***")
dis.dis(f)
print("g disclosure ***")
dis.dis(result)