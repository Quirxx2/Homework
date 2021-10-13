def get_digits(num):
    a = list()
    for i in str(num): a.append(int(i))
    return tuple(a)

s = 348478389289

print(get_digits(s))
