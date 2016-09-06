def main(fn):
    fn()
    return fn

def cube(x):
    return x * x * x
    
def run_tests():
    print("Should be 1:", cube(1))
    print("Should be 8:", cube(2))
    print("Should be 27:", cube(3))
   
@main:
def main():
    print("Starting. ")
    run_tests()
    print("Ending. ")