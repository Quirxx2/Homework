class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print("{0} bird can fly".format(self.name))

    def walk(self):
        print("{0} bird can walk".format(self.name))

    def str(self):
        print("{0} bird can walk and fly".format(self.name))


class FlyingBird(Bird):

    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print("It eats mostly {0}".format(self.ration))


class NonFlyingBird(Bird):

    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    @property
    def fly(self):
        raise AttributeError("{0} object has no attribute 'fly'".format(self.name))

    def eat(self):
        print("It eats mostly {0}".format(self.ration))

    def swim(self):
        print("{0} bird can swim".format(self.name))

    def str(self):
        print("{0} bird can walk and swim".format(self.name))


class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)

    def eat(self):
        print("It eats {0}".format(self.ration))

    def str(self):
        print("{0} bird can walk, swim and fly".format(self.name))

b = Bird("Any")
b.walk()
#"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
p.swim()
#"Penguin bird can swim"
#p.fly()
#AttributeError: 'Penguin' object has no attribute 'fly'
p.eat()
#"It eats mostly fish"

c = FlyingBird("Canary")
c.str()
#"Canary bird can walk and fly"
c.eat()
#"It eats mostly grains"

s = SuperBird("Gull")
s.str()
#"Gull bird can walk, swim and fly"
s.eat()
#"It eats fish"