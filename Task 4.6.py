def get_shortest_word(s):
    b = list()
    c = list()
    for i in range(len(s)):
        # skip spaces
        if s[i] == ' ':
            continue
        else:
            index = i
            break
        # read one another word
        while True:
            b.append(s[index])
            index += 1
            if s[index] == ' ':
                i = index - 1
                c.append(str(b))
                print(c)
                b.clear()
                break
    index2 = 1
    for i in range(len(c)):
        if len(c[i]) > len(c[index2]):
            index2 = i
    return c[index2]

s1 = 'Python is simple and effective!'

print(get_shortest_word(s1))