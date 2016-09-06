d1 = {'me': 2, 'call': 3, 'may be': 3}

def make_inverse_dict_iter(d1):
    d2 = {}
    for key in d1:
        if d2.get(d1[key]) == None:
           d2[d1[key]] = (key,)
        else:
            d2[d1[key]] += (key,)
    return d2

#d2 = make_inverse_dict_iter(d1)

def make_inverse_dict_recur(d1):
    temp = {}
    def make_inverse_dict():
        if d1:
            key, val = d1.popitem()
            if temp.get(val) == None:
                temp[val] = (key, )
            else:
                temp[val] += (key, )			
            make_inverse_dict()
    make_inverse_dict()
    return temp

d2 = make_inverse_dict_recur(d1.copy())