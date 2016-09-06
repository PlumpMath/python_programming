def account():
    def withdraw(amount):
        if amount > dispatch['balance']:
           return 'Insufficient funds'
        dispatch['balance'] -= amount;
        return dispatch['balance']
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    dispatch = {'balance': 0,
                'withdraw': withdraw,
                'deposit': deposit}
    return dispatch	

a = account()
a['deposit'](20)
a['withdraw'](10)
a['balance']

