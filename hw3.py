a = ['1.txt', '2.txt', '3.txt']
x = {}
for i in a:
    with open(i) as file:
        f = file.readlines()
        x[i] = [len(f), ''.join(f)]



x = dict(sorted(x.items(), ))

with open('res.txt', 'w', 'encoding=utf-8') as file:
    for i, j in x.items():
        z = [i] + j
        print(z)