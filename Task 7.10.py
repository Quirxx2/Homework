def endless_generator():
    count = -1
    while True:
        count += 2
        yield count


gen = endless_generator()
while True:
    print(next(gen))
# 1 3 5 7 ... 128736187263 128736187265 ...
