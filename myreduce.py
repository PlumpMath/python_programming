def myreduce(func, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = func(tally, next)
    return tally

result = myreduce((lambda x, y: x * y), [1, 2, 3, 4])
print(result)