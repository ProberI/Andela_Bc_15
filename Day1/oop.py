class Counter(object):
    num = 0

    def __init__(self):
        type(self).number += 1


class Account(Counter):  # inheritance

    def __init__(self, account_holder, account_number, balance, acc_current=1500):
        Counter.__init__(self)
        self.public = account_holder  # Encapsulation
        self.public = account_number
        self.public = balance
        self.public = acc_current

    def deposit(self):  # Abstraction
        amount = float(input("Please input amount to deposit"))
        if amount > 0:

            self.balance += amount
        else:
            return 'Please enter valid deposit amount'


