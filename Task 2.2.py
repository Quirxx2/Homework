s = 'Oh, it is python'

dictS = {}

for i in s:
    i = i.lower()
    print(i)
    if i in dictS:
        dictS[i] += 1
    else:
        dictS[i] = 1

print(dictS)
