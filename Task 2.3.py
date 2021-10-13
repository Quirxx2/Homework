s1 = 'red,white,black,red,green,black'

# print(s1)

s2 = s1.split(',')

# print(s2)

s3 = set(s2)

# print(s3)

s4 = list(s3)

s4.sort()

print(s4)