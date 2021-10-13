a = int(input())
b = int(input())
c = int(input())
d = int(input())

maxlens = len(str(b*d))

s = " " * maxlens

e = [[s for j in range(d - c + 3)] for i in range(b - a + 3)]

for i in range(d - c + 2):
    e[0][i + 1] = str(c + i)

for j in range(b - a + 2):
    e[j + 1][0] = str(a + j)

for i in range(b - a + 2):
    for j in range(d - c + 2):
        e[i + 1][j + 1] = str(int(e[i + 1][0]) * int(e[0][j + 1]))

for i in range(b - a + 2):
    for j in range(d - c + 2):
        print(e[i][j].ljust(maxlens), end=' ')
    print()





