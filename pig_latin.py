def pig_latin(w):
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin(w[1:] + w[0])

def is_vowel(w):
   return w[0].lower() in 'aeiou'	