a = ['1.txt', '2.txt', '3.txt']
x = {}
for i in a:
    with open(i) as file:
        f = file.readlines()
        x[i] = [len(f), ''.join(f)]


x = dict(sorted(x.items(), key=lambda i: i[1][0]))

with open('res.txt', 'w') as file:
    for i, j in x.items():
        xxx = [i] + j
        print(*xxx, sep='\n', file=file)
