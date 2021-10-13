f = open('data/unsorted_names.txt', 'r')
l = [line.strip() for line in f]
f.close()

l.sort()

f = open('data/sorted_names.txt', 'w')
for i in l:
    f.write(i + '\n')

f.close()