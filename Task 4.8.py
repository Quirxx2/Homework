def getpairs(s):
    d = list()
    for i in range(len(s) - 1):
        d.append((s[i], s[i + 1]))
    return d


print(getpairs([1, 2, 3, 8, 9]))