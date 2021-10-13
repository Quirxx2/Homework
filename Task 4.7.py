def foo(s):
    d = list()
    mpx = 1
    for j in s:
        mpx *= j
    for i in s:
        d.append(mpx // i)
    return d


l1 = [1, 2, 3, 4, 5]
l2 = [3, 2, 1]

print(foo(l1))
print(foo(l2))


