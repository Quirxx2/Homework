def swapsymbols(s):
    l = list()
    for i in s:
        if i == "\'":
            l.append("\"")
            continue
        elif i == '"':
            l.append('\'')
            continue
        l.append(i)
    str1 = ''.join(l)
    return str1

a = 'Mister\'s party is held on the "3" floor'

print(a)
print(swapsymbols(a))