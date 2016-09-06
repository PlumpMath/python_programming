def count_calls(f):
    """ A function that returns a version of f that counts calls to f
    and can report that count how_many_calls"""
    count = 0
    def counted_add(x, y):
        nonlocal count
        count = count + 1
        return f(x, y)
    def add_count():
        return count
    return counted_add, add_count