string = 'AABCAAADAC'
k = 2

for part in zip(*[iter(string)] * k):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
