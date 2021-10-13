def strsplit(s, splitter, maxsplit=-1):
    cx = list()
    count = 0
    i = 0
    while True:
        if (count > (maxsplit - 1)) and (maxsplit != -1):
            cx.append(s)
            return cx
        if (len(s) - i) >= len(splitter):
            ax = s[i:(i+len(splitter))]
            if ax == splitter:
                bx = s[:i]
                cx.append(bx)
                s = s[(i+len(splitter)):]
                count += 1
                i = 0
        else:
            cx.append(s)
            return cx
        i += 1

s = 'mango, orange, cherry, apple, strawberry, papaya, melon'

print(s)

print(strsplit(s, ', ', 3))
print(strsplit(s, ', ', ))
print(strsplit(s, ', ', 10))

