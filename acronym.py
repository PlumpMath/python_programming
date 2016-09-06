def first(s):
    return s[0]

def iscap(s):
    return len(s) > 0 and s[0].isupper()

def acronym(name):
    """Return a tuple of the letters that form the acronym for name.
	
	>>> acronym('University of California Berkeley')
	('U', 'C', 'B')
	"""
    return tuple(map(first, filter(iscap,name.split())))

def acronym_gen(name):
    """Return a tuple of the letters that form the acronym for name.
	
	>>> acronym_gen('University of California Berkeley')
	('U', 'C', 'B')
	"""
    return tuple(w[0] for w in name.split() if iscap(w))