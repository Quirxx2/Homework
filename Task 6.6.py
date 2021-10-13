#import functools

#@functools.total_ordering
class Money:

    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.new_amount = 0
        self.currency = currency
        self.exchange_rate = {
            "EUR": 0.93,
            "BYN": 2.1,
            "USD": 1.0,
            "JPY": 97.93
        }

    def __add__(self, other):
        self.new_amount = self.amount + other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]
        return Money(self.new_amount, self.currency)

    def __radd__(self, other):
        if type(other) != type(self):
            other = Money(0)
        self.new_amount = self.amount + other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]
        return Money(self.new_amount, self.currency)

    def __sub__(self, other):
        self.new_amount = self.amount - other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]
        return Money(self.new_amount, self.currency)

    def __rsub__(self, other):
        self.new_amount = other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency] - self.amount
        return Money(self.new_amount, self.currency)

    def __mul__(self, other):
        self.new_amount = self.amount * other
        return Money(self.new_amount, self.currency)

    def __rmul__(self, other):
        self.new_amount = self.amount * other
        return Money(self.new_amount, self.currency)

    def __truediv__(self, other):
        self.new_amount = self.amount / other
        return Money(self.new_amount, self.currency)

    def __rtruediv__(self, other):
        self.new_amount =  other / self.amount
        return Money(self.new_amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]

    def __lt__(self, other):
        return self.amount < other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]

    def __le__(self, other):
        return self.amount <= other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]

    def __ne__(self, other):
        return self.amount != other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]

    def __gt__(self, other):
        return self.amount > other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]

    def __ge__(self, other):
        return self.amount >= other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]

    def __repr__(self):
        return f'{round(self.amount, 2)} {self.currency}'


x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
#>>34.3 EUR

lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
#>>33.36 BYN