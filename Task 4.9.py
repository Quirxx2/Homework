import string

def test_1_1(*strings):
    l = list()
    for i in strings:
        for j in i:
            s = set(str(j))
            l.append(s)
    s = l[0]
    for i in l:
        s = s & i
    return s

def test_1_2(*strings):
    l = list()
    for i in strings:
        for j in i:
            s = set(str(j))
            l.append(s)
    s = l[0]
    for i in l:
        s = s | i
    return s

def test_1_3(*strings):
    l = list()
    t = set()
    for i in strings:
        for j in i:
            s = set(str(j))
            l.append(s)
    n = set()
    for i in range(len(l)):
        for j in range(len(l)):
            if j != i:
                t = l[j] & l[i]
                n = n | t
    return n

def test_1_4(*strings):
    return set(string.ascii_lowercase) - test_1_1(strings)

test_strings = ["hello", "world", "python", ]

print(test_1_1(test_strings))

print(test_1_2(test_strings))

print(test_1_3(test_strings))

print(test_1_4(test_strings))