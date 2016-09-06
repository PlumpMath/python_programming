def expt(base, power):
    if power == 1:
        return base
    else:
        return base * expt(base, power -1)