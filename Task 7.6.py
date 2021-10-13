import math


class MyError(Exception):

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


MAX = 10000
primes = []


def even(number):

    if number < 3:
        raise MyError('The number is too small.')
    if number % 2 != 0:
        raise MyError('The number is odd.')
    return True

def sievesundaram():

    marked = [False] * (int(MAX / 2) + 100)

    for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
        for j in range((i * (i + 1)) << 1,
                       int(MAX / 2) + 1, 2 * i + 1):
            marked[j] = True
    primes.append(2)

    for i in range(1, int(MAX / 2) + 1):
        if (marked[i] == False):
            primes.append(2 * i + 1)


def findprimes(n):

    i = 0
    while (primes[i] <= n // 2):

        diff = n - primes[i]
        if diff in primes:
            print(primes[i], "+", diff, "=", n)
            return
        i += 1


sievesundaram()

try:
    while True:
        print('input test number, "q" to exit')
        test_number = input()
        if test_number == 'q':
            break
        try:
            t_number = int(test_number)
        except:
            raise MyError('Input is not a number.')
        if even(t_number):
            findprimes(t_number)
except MyError as e:
    print("New exception has been called:", e.msg)

