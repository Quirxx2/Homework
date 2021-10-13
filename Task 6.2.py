class HistoryDict:

    def __init__(self, item):
        self.d = item
        self.my_deque = []
        self.my_deque2 = []
        self.count = 0
        self_limit = 10
        for key in self.d.keys():
            self.my_deque.append(key)
            self.count += 1

    def set_value(self, key, value):
        self.d[key] = value
        self.count += 1
        if (key in self.my_deque) and (self.count > self.limit):
            self.count -= 1
            self.my_deque.remove(key)
            self.my_deque.append(key)
        elif key in self.my_deque:
            self.my_deque.remove(key)
            self.my_deque.append(key)
        else:
            self.my_deque.append(key)

    def get_history(self):
        self.my_deque2 = self.my_deque.copy()
        self.my_deque2.reverse()
        return self.my_deque2


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())
