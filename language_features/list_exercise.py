>>> lst = [(1,2), (3,4)]
>>> lst.append((5, 6))         #  [(1,2), (3,4), (5, 6)]
>>> lst.clear()                #  []
>>> lst1 = [(1,2), (3, 4)] 
>>> lst2 = lst1.copy()     """ lst1 ------->[  |    ,  |  ] 
                                               |       | 
                                               V       V 
                                            (1, 2)  (3, 4) 
                                               ^       ^
					                                     |       |
					                                     |       |
					                      lst2------->[  |    ,  | ]  shallow copy
					   
              					   """
>>> lst1.count((1, 2))        #  1 occurence

""" 
1) A container is said to be iterable if it has the __iter__ method defined.
2) Iterable - A container is said to be iterable if it has the __iter__ method defined.
3) Iterator - An iterator is an object that supports the iterator protocol which 
              basically means that the following two methods need to be defined.
           a) It has an __iter__ method defined which returns itself.
           b) It has a next method defined (__next__ in Python 3.x) which returns 
          		      the next value every time the next method is invoked on it.
"""

>>> a = [1, 2, 3, 4]
>>> # a list is iterable because it has the __iter__ method
>>> a.__iter__
<method-wrapper '__iter__' of list object at 0x014E5D78>
>>> # However a list does not have the next method, so it's not an iterator
>>> a.next
AttributeError: 'list' object has no attribute 'next'
>>> # a list is not its own iterator
>>> iter(a) is a    # is checks for object identity. It returns true if two names refer to the same object. 
False

#The iterator of a list is actually a listiterator object. A listiterator is its own iterator.
>>> # a iterator for a list is actually a 'listiterator' object
>>> ia = iter(a)
>>> ia
<listiterator object at 0x014DF2F0>
>>> # a listiterator object is its own iterator
>>> iter(ia) is ia
True

#Extends any iterable
>>> lst1 = [123, "xyz"]
>>> lst1.extend(1.5)
    TypeError: 'float' object is not iterable
>>> lst1 = [(1, 2), (3, 4)]
>>> tup = ((5, 6),)
>>> lst1.extend(tup)   # [(1, 2), (3, 4), (5, 6)]

>>> lst1.index((1,2), 0, 1)    # 0
>>> lst1.index((3,4), 0, 2)    # 1

>>> lst1 = [1, 2, 3]
>>> lst1.insert(3, 4)   # insert object before index 4
>>> lst1
[1, 2, 3, 4]
>>> lst1.pop(0)         # Removes and return item at index 0
1
>>> lst1.remove(4)      # [2, 3]; Removes value
>>> lst1.reverse()      # [3, 2]; IN PLACE reverse
>>> lst1.sort()         # [2, 3]; IN PLACE stable sort