class Door:
    def __init__(self,closed=False):
        self.closed=closed

    def open(self):
        if not self.closed:
            print("door is already opened!")

        self.clsoed=False

            else self.close


    def close(self):
        pass




door=Door()
door.open()
door.open()
door.close()
door.close()



'''
    class BankAccount:
        def __init__(self, initial_balance=0):
            self.balance = initial_balance

        def deposit(self, amount):
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            self.balance += amount
'''