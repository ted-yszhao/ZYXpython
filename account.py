from math import log , ceil

class Account:

    # class attribute
    interest = 0.02

    def __init__(self,name): # helper for construction
        # special method 


        # instance attribute
        self.balance = 0
        self.holder = name

    def deposit(self,amount):
        assert amount > 0
        self.balance += amount

    # method 
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient fund.'
        else:
            self.balance -= amount
            return self.balance
        
    # special function
    def __eq__(self, value): # return bool 
        return isinstance(value,Account) and value.holder == self.holder
    
    def __repr__(self):
        """
            Account(name)
        """

        return f'Account({self.holder})'


    def __str__(self):
        """
            Bank Accout:
                holder: name
                balance: $ 
        """

        return f"Bank Account\nholder: {self.holder}\nbalance: ${self.balance:.2f}\n"

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        current_balance,year=self.balance,0
        while current_balance<amount:
            current_balance*=(1+self.interest)
            year+=1
        return year

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!

    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free. Still counts as a free withdrawal even though it was unsuccessful
    'Insufficient funds'
    >>> ch.withdraw(3)    # Second withdrawal is also free
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Now there is a fee because free_withdrawals is only 2
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """

    # class attribute 
    withdraw_fee = 1
    free_withdrawals = 2
    def __init__(self,name):
        super().__init__(name)
        self.free_withdrawls_remaining=self.free_withdrawals

    def withdrawals(self,amount):
        if self.free_withdrawals_remaining>0:
            self.free_withdrawals_remaining-=1
            return super().withdraw(amount)
        else:
            return super().withdraw(amount+self.withdraw_fee)
        
    "*** YOUR CODE HERE ***"


# Is-a relationship 

# CheckingAccount is a sub-class of Account
# Account is a super class of CheckingAccount

# Sup class will inherit all attributes and method from its super 
class CheckingAccount(Account): 
    # new attribute 
    withdraw_charge = 1
    

    # overriding 覆盖
    interest = 0.01

    # method overriding
    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_charge)
        # return Account.withdraw(self,amount+self.withdraw_charge)
        

class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return super().deposit(amount - self.deposit_charge)
        
class AsSeenOnTVAccount(CheckingAccount,SavingsAccount):
    def __init__(self, name):
        self.holder = name
        self.balance = 1 # reward for opening account

    

ben = Account('Ben')
ben.deposit(100)

print(ben)
    
