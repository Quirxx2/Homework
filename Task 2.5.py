l = {'dd': '001', 'ac': '002', 'bb': '003', 'aa': '004', 'bn': '005', 'ph': '006', 'kl': '007'}

print(l)

result = {}

for k in sorted(l):
    result[k] = l[k]

print(result)
