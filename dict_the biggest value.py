d = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
l = sorted(d.items(), reverse=True, key=lambda para: para[1])
l1 = l[0:3]
for i in l1:
    print(i)