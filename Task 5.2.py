def most_common_words(filepath, number_of_words = 3):
    f = open(filepath, 'r')
    t = f.read()
    f.close()
    s = []
    d = {}
    for i in t:
        if i.isalpha():
            s.append(i.lower())
        else:
            key = ''.join(s)
            if key in d:
                d[key] += 1
            else:
                if len(key) != 0:
                    d[key] = 1
            s.clear()
    sorted_tuples = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return list(map(lambda x: x[0], sorted_tuples[:number_of_words]))


print(most_common_words('data/lorem_ipsum.txt'))
