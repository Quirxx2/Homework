n = int(input())    # число, до которого хотим найти проn = int(input())

s = []
i = 1
while i <= n:
    if n % i == 0:
        s.append(i)
    i+=1

print(s)