t = (1, 2, 3, 4, -5, 9, -2, 3)
s = ''

for i in t:
    if i > 0:
        s = s + str(i)

i = int(s)
print(i)