def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    incorrect_password_list = []
    count = 0
    def withdraw(amount, input_passwd):
        nonlocal count
        if count < 3:
            if input_passwd == password
                nonlocal balance
                if  amount < balance:
                    balance -= amount
                    return balance			
                else:
                    return "Insufficient funds"
            else:
                nonlocal incorrect_password_list
                incorrect_password_list.append(input_passwd)
                count += 1				
                return "Incorrect password"
        else:
            return "Your account is locked. Attempts: ['{0}', '{1}', '{2}']".format(incorrect_password_list[0], incorrect_password_list[1], incorrect_password_list[2])
    return withdraw