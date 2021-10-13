def get_top_performers(file_path, number_of_top_students=5):
    f = open(file_path, 'r')
    l1 = [line.strip() for line in f]
    f.close()
    l2 = []
    for i in range(len(l1)):
        l2.append(list(map(str, l1[i].split(','))))
    l2.pop(0)
    l2.sort(key = lambda x: float(x[2]), reverse=True)
    return list(map(lambda x: x[0], l2[:number_of_top_students]))

def put_most_older(file_path):
    f = open(file_path, 'r')
    l1 = [line.strip() for line in f]
    f.close()
    l2 = []
    for i in range(len(l1)):
        l2.append(list(map(str, l1[i].split(','))))
    l3 = l2[0]
    l2.pop(0)
    l2.sort(key = lambda x: int(x[1]), reverse=True)
    f = open("data/students_new.csv", 'w')
    r = l3[0] + ',' + l3[1] + ',' + l3[2]
    f.write(r + '\n')
    for i in l2:
        r = i[0] + ',' + i[1] + ',' + i[2]
        f.write(r + '\n')
    f.close()


print(get_top_performers("data/students.csv"))
put_most_older("data/students.csv")