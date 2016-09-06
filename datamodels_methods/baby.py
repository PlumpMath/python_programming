def find_ratio(input, word):
    """ 
    >>> diane_young = "baby baby baby baby right on time"
    >>> find_ratio(diane_young, "baby")
    "4 to 7"
    >>> baby = "like baby baby baby no like baby baby baby oh"
    >>> find_ratio(baby, "baby")
    "6 to 10"	
    """
    list_of_words = input.split()
    count_all = len(list_of_words)
    count_word =  len([x for x in list_of_words if x == word])
	return "{0} to {1}".format(count_word, all)