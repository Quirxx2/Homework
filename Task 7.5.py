class MyError(Exception):

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


def even(number):

    if number < 3:
        raise MyError('The number is too small.')
    if number % 2 != 0:
        raise MyError('The number is odd.')
    return True


try:
    while True:
        print('input test number, -1 to exit')
        test_number = int(input())
        if test_number == -1:
            break
        if even(test_number):
            print('The number is even')
except MyError as e:
    print("New exception has been called:", e.msg)
