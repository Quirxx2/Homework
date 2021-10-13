def generate_squares(num):
    d = {a: a**2 for a in range(1, num + 1)}
    return d


print(generate_squares(5))
