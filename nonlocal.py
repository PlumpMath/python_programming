def f(lst):
    def g():
        print('In g()' + str(lst))
        def h():
            nonlocal lst
            lst = [1, 2, 3]
            print('In h()' + str(lst))
        return h()
    g()
    print('In f()' + str(lst))	

f([1, 2, 3, 4])