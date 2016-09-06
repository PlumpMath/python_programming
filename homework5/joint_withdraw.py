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
            if input_passwd == password:
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

def make_joint(withdraw, old_passwd, new_passwd):
    """
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'
    """
    value = withdraw(0, old_passwd)
    if type(value) == str:
        return "Incorrect password"
    else:
        def joint_withdraw(balance, input_passwd):
            if (input_passwd ==  old_passwd) or (input_passwd ==  new_passwd):
                return withdraw(balance, old_passwd)
        return joint_withdraw