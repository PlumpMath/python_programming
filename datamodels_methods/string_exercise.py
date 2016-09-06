# In python 3, strings are not bytes.
# Strings are Unicode (which are not bytes) Unicode strings use "..." or '...'
# Bytes are bytes (which are not strings) Byte strings use b"..." or b'...'
# Only ASCII characters are permitted in bytes literals
"abc".center(10,'x')
"abc".capitalize()              # 'Abc'
"ABc".casefold()                # 'abc'
"ABC".casefold()                # 'abc'
"abc".center(10,'x')            # 'xxxabcxxxx'
str = 'mississippi'
str.count('issi')               #  1; non-overlapping occurrences
str.count('issi',1, 5)          #  1; arg: start_index, end_index+1


#In Python 3.x all strings are Unicode by default
#Converting python strings to bytes, and bytes to strings
nonlat = '字'
ord(nonlat)                     #  23383; ordinal, which means a number defining a position in Unicode
chr(23383)                      #  '字'; Gives unicode character
bytes(nonlat, 'utf-8')			#  b'\xe5\xad\x97'; It means that the single character contained 
                                #  in our nonlat variable was effectively translated into a string of code that means "字" in UTF-8
bytes(nonlat, 'utf-16')         #  b'\xff\xfeW['
nonlat.encode()					#  b'\xe5\xad\x97'; Indeed we got the same result, but we did not give encoding in this case.
nonlat.encode('utf-16')			#  b'\xff\xfeW['
b'\xff\xfeW['.decode('utf-16')  #  '字'
#Writing non-ASCII Data to Files in Python 3.x
with open('nonlat.txt', 'wb') as f:
    f.write(nonlat.encode())    #  read with 'rb' mode


"abc".endswith('c')             #  True
"abc".endswith('c', 2, 3)       #  True
"a	b".expandtabs(4)            #  'a   b'
"a	b".expandtabs(8)            #  'a       b'
'a bc'.find(' bc')              #  1
'{0} in hex is {1}'.format('字', hex(ord('字')))   # '字 in hex is 0x5b57'
'{0} in hex is {1:X}'.format('字', ord('字'))      # '字 in hex is 5B57'
new_people = [
    {'age': 56, 'name': 'john'},
    {'age': 64, 'name': 'peter'}
]
for d in new_people:
    print('My name is {0}, I am {1} years old.'.format(d['name'], d['age']))   #  My name is john, I am 56 years old.
                                                                               #  My name is peter, I am 64 years old.
'abc'.index('bc', 1, 3)         #  1
'abc12'.isalnum()               #  True
'abc12'.isalpha()               #  False
'10'.isdecimal()                #  True
'0x10'.isdecimal()              #  False
'12346a'.digit()                #  False; If all the characters in the string are digits
'abc'.isidentifier()            #  True; If s is non empty and is a valid identifier
'ABC'.islower()                 #  False; If all the case-based characters (letters) of the string are lower case.  
'abc209'.isnumeric()            #  False; If all characters in the string are numeric
chr(7).isprintable()            #  False; bell character is not printable
chr(23383).isprintable()        #  True;  '字' is printable
'abc'.isspace()                 #  False
'    '.ispace()                 #  True
'An Example..Wow!!'.istitle()   #  True; if string is title cased string
'An example..Wow!!'.istitle()   #  False
'Abc'.isupper()                 #  False
separator = '**'
seq = ['a', 'b', 'c']
separator.join(seq)             #  'a**b**c'
'abc'.ljust(10, '*')            #  'abc*******'; left justify with width-10 and fill the character '*'
'Abc'.lower()                   #  'abc'
str = '98dfgfd'
str.lstrip('89')                #  'dfgfd'; '89' are string of chars to be stripped on starting only.
'word1 word2'.partition(' ')    #  ('word1', ' ', 'word2'); returns (head, sep, tail)
                                  #  Split the string at the first occurrence of sep, and return a 3-tuple
                                #  containing the part before the separator, the separator itself, and 
                                #  the part after the separator. If the separator is not found, return 
                                #  a 3-tuple containing the string itself, followed by two empty strings.
'word1 word2'.split(' ')        #  ['word1', 'word2']; returns list of strings
intab = '字aeiou'
outtab = '612345'
s = '字this is string example....wow!!!'
print(s.translate({ord(x): y for (x, y) in zip(intab, outtab)}))    #  '6th3s 3s str3ng 2x1mpl2....w4w!!!'


'abcabcabc'.replace('ab', 'xy', 2)    #  'xycxycabc'
'abcabcabc'.rfind('bc', 0, 9)         #  7; find starts from the end
'abcabcabc'.rfind('x', 0, 9)          #  -1; if not found
'abcabcabc'.rindex('x', 0, 9)         #  raises ValueError exception
'abc'.rjust(10, '*')                  #  '*******abc'
'abc'.rpartition(' ')                 #  ('', '', 'abc')
                                      #  Split the string at the last occurrence of sep, and return a 3-tuple
                                      #  containing the part before the separator, the separator itself, and 
                                      #  the part after the separator. If the separator is not found, return 
                                      #  a 3-tuple containing two empty strings, followed by the string itself.
'abc,defg,hij'.rsplit(',', 1)         #  Split the string at the last occurrence of sep, and return a 3-tuple
                                      #  containing the part before the separator, the separator itself, and 
                                      #  the part after the separator. If the separator is not found, return
                                      #  a 3-tuple containing two empty strings, followed by the string itself.
str = 'Line1- a b c d e f\nLine2 - a b c\n\nLine4- a b c d'           
str.splitlines(True)                  #  ['Line1- a b c d e f\n', 'Line2 - a b c\n', '\n', 'Line4- a b c d']
str.splitlines(False)                 #  ['Line1- a b c d e f', 'Line2 - a b c', '', 'Line4- a b c d']
                                      #  if you want each line to include the break sequence (CR,LF,CRLF),
                                      #  use the splitlines method with a True argument.
'abc'.startswith('a')                 #  True
'8ab9c8a9b8c89'.strip('89')           #  'ab9c8a9b8c'
'Abc'.swapcase()                      #  'aBC'
'this is example'.title()             #  'This Is Example'
'23abc45'.upper()                     #  '23ABC45'
'abc'.zfill(10)                       #  '0000000abc'; zero fill
'here' in "Where's Waldo?"            #  True
print('\a')                           #  bell

from unicodedata import lookup, name
name('a')                             #  'LATIN SMALL LETTER A';     This is canonical name.
name('字')							  #  'CJK UNIFIED IDEOGRAPH-5B57' 
lookup('THAI CHARACTER KHOMUT')       #      '๛'
len('字๛')                            #   2; Return the length (the number of items) of an object. The argument
                                      #   may be a sequence (such as a string, bytes, tuple, list, or range) or
                                      #   a collection (such as a dictionary, set, or frozen set.

dir('abc')                            #  Gives the  list of attributes for object of type <class 'str'>

