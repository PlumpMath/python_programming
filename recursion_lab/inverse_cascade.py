def inverse_cascade(n):
    def grow(n):
        if n < 10:
            print(n)
        else:
            grow(n // 10)
            print(n)
    def shrink(n):
        if n < 10:
            print(n)
        else:
            print(n)
            shrink(n // 10)
    grow(n // 10)
    print(n)
    shrink(n // 10)