def reverse(str):
    if str == '':
        return '' 
    return reverse(s[1:]) + s[0]