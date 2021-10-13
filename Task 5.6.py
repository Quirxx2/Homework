def call_once(func):
    flag = False

    def counter(a, b):
        nonlocal flag
        if flag is not True:
            counter.first_res = func(a, b)
            flag = True
            return counter.first_res
        return counter.first_res
    return counter


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
# 55
print(sum_of_numbers(999, 100))
# 55
print(sum_of_numbers(134, 412))
# 55
print(sum_of_numbers(856, 232))
# 55
