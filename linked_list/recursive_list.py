##################
#   Linked List  #
##################



#Representation - start
empty = 'empty'
def is_link(s):
    """ s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (isinstance(s, list) and len(s) == 2 and is_link(s[1]))
#Constructor
def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list"
    return [first, rest]
#Selector 1
def first(s):
    """Return a first element of a linked list s"""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]
#Selector 2
def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def isempty(s):
    return s == empty

#Representation - end

###  +++ === Abstraction barrier === +++ ###

#Use(interface) -  start
def create_linked_list(first, rest):
    return link(first, rest)

def len_rlist(s):
    """Compute the length of the recursive list s"""
    if isempty(s):
        return 0
    else:
        return 1 + len_rlist(rest(s))


def getitem_rlist(s, i):
    """Return the element at index i of recursive list s"""
    if i == 1:
        return first(s)
    else:
        return getitem_rlist(rest(s), i-1)

def count(s, value):
    """Count the occurence of value in the list s """
    if isempty(s):
        return 0
    else:
        if first(s) == value:
            return 1 + count(rest(s), value)
        else:
            return count(rest(s), value)

def extend(s, t):
    if isempty(rest(s)):
        return t
    extend(rest(s), t)
#Use - end


#Constructor and Selector constitutes Abstract Data Type that supports below invariants:
#If a recursive list s is constructed from a first element f and a recursive list r, then
#   • first(s) returns f, and
#   • rest(s) returns r, which must be a list or 'empty'.

#Code using this abstraction
Lst = empty
Lst = create_linked_list(4, Lst)   #  Representation [4, 'empty']
Lst = create_linked_list(3, Lst)   #  Representation [3, [4, 'empty']]
Lst = create_linked_list(1, Lst)   #  Representation [1, [3, [4, 'empty']]]
Lst = create_linked_list(1, Lst)   #  Representation [1, [1, [3, [4, 'empty']]]]
print(count(Lst, 1))