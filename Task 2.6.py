l = ({'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'})

s = set()

for i in l:
    for value in i.values():
        s.add(value)

print(s)
