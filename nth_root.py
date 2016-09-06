def approx_deriv(fn, x, dx=0.00001):
    return (fn(x + dx) - fn(x))/dx

def improve(update, isdone, guess=1, max_iterations=100):
    def recur_improve(guess, i):
        if i > max_iterations or isdone(guess):
           return guess
        else:
           return recur_improve(update(guess), i + 1)
    return recur_improve(guess, 1)

def newtons_method(fn, guess =1, max_iterations=100):
    def newtons_update(guess):
        return guess - fn(guess) / approx_deriv(fn, guess)
    def newtons_isdone(guess):
        ALLOWED_ERROR_MARGIN = 0.0000001
        return abs(fn(guess)) <= ALLOWED_ERROR_MARGIN
    return improve(newtons_update, 
                        newtons_isdone, 
                        max_iterations)