def sum_range(given_min, given_max):
    """
    >>> sum_range(45, 60) # Printer A prints within this range;
    True
    >>> sum_range(40, 55) # Printer A can print some number 56-60
    False
    >>> sum_range(170, 201) # Printer A + Printer B will print somewhere between 180 and 200 copies total
    True
    """
    def helper(print_min, print_max):
        if print_min >= given_min and print_max <= given_max:
            return True
        if print_min and  (print_min < given_min or print_max > given_max):
            return False
        return helper(50 + print_min, 60 + print_max) or helper(130 + print_min, 140 + print_max) or helper(50 + 130 + print_min, 60 + 140 + print_max)
    return helper(0, 0)