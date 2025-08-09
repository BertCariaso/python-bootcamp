class Payment:
    def __init__(self,amount):
        self.amount=amount

    def valid(self):
        return self.amount >0

class Coupon:
    def __init__(self,amount, expired):
        self.amount=amount
        self.expired=expired

    def valid(self):
        return not self.expired and self.amount>0

class Coupon(Payment):
    def __init__ (self, amount, expired):
        super().__init__ (amount)
        self.expired=expired

    def valid(self):
        return not self.expired and super().valid()


class Card_Payment(Payment):
    def __init__ (self, amount,card_number):
       super().__init__(amount)
       self.card_number=card_number

    def valid(self):
        is_16_digits=self.card_number.isnumeric() and len(self.card_number)==16
        return is_16_digits and super().valid()

    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense


class OnlinePayment(Payment):
    def __init__(self,amount,email):
            super().__init__(amount)
            self.email=email
    def valid(self):
        return self.email.endswith('gmail.com') and super().valid()


