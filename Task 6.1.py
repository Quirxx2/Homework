class Counter:
    counter = 0
    limit = -1

    def __init__(self, start=0, stop=-1):
        self.counter = start
        self.limit = stop

    def increment(self):
        if self.counter == self.limit:
            raise Exception('Maximal value is reached.')
        self.counter += 1

    def get(self):
        return self.counter


a = Counter(start=42)
a.increment()
print(a.get())

b = Counter()
b.increment()
print(b.get())

b.increment()
print(b.get())

c = Counter(start=42, stop=43)
c.increment()
print(c.get())

c.increment()
print(c.get())

