d = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
for i in sorted(d.items(), reverse=True, key=lambda para: para[1]):
    print(i)

