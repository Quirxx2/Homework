def endless_fib_generator():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


gen = endless_fib_generator()

while True:
    print(next(gen))
