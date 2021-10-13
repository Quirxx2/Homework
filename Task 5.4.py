a = "I am global variable!"


def enclosing_function1():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    return inner_function


def enclosing_function2():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a

        print(a)

    return inner_function


def enclosing_function3():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a

        print(a)

    return inner_function

x = enclosing_function1()()
x = enclosing_function2()()
x = enclosing_function3()()



