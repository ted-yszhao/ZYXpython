class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        """Set the product and its price, as well as other instance attributes."""
        # stock 
        # product : str
        # price : int
        # balance ： int
        self.stock = 0
        # instance attribute
        self.product = product
        self.price = price
        self.balance = 0


    def restock(self, n):
        """Add n to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        """
        self.stock+=n
        return f"Current {self.product} stock: {self.stock}"
        
        

    def add_funds(self, n):
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Nothing left to vend. Please restock. Here is your $4.

        Otherwise, add n to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        """
        if self.stock==0:
            return f"Nothing left to vend. Please restock. Here is your ${n}."
        else:
            self.balance += n
            return f'Current balance: ${self.balance}'

        

    def vend(self):
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Nothing left to vend. Please restock.
              Please add $3 more funds.
        """
        if self.stock==0:
            return "Nothing left to vend. Please restock."
        elif self.balance<self.price:
            return f"Please add ${self.price-self.balance} more funds."
        else:
            self.stock-=1
            change=self.balance-self.price
            self.balance=0
            if change==0:
                return f"Here is your {self.product}."
            else:
                return f"Here is your {self.prodct} and ${change} change."