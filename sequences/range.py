# A range is a sequence of consecutive integers
range(-2, 2)          # length = ending value - starting value = 4; -2 -1 0 1
r1 = range(-2, 2)
r1[0]                  # -2; 
r2 = range(4)
r2[0]                  # 0;
r2[3]				   # 3;

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears')

