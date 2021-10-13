def split_by_index(s, indexes):
    l = list()
    old_i = 0
    for i in indexes:
        delta = i - old_i
        if delta <= len(s):
            l.append(s[:delta])
            s = s[delta:]
            old_i = i
        else:
            l.append(s[:delta])
            break
    return l


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18, 21]))

print(split_by_index("no luck", [42]))