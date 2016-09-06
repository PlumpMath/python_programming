def min_element_recur(tup):
    if len(tup) == 1:
       return tup[0]
    elif len(tup) >= 2:
       a = tup[0]
       b = min_element_recur(tup[1:])
       return a if a < b else b