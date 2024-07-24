

def strings():
    with open ('1.txt', encoding='utf-8') as f:
        for idx_1, l in enumerate(f):
            print (idx_1, l.strip())

    with open ('2.txt', encoding='utf-8') as f:
        for idx_2, x in enumerate(f):
            print (idx_2, x.strip())

    with open ('3.txt', encoding='utf-8') as f:
        for idx_3, a in enumerate(f):
            print (idx_3, a.strip())

    for k in strings():
        if idx_1[-1] > idx_2[-1] > idx_3[-1]:
            print(f'[3.txt\n 1, \n 2.txt/n 2, \n 1.txt\n 3]')
        elif idx_2[-1] > idx_1[-1] > idx_3[-1]:
            print(f'[3.txt\n 1, \n 1.txt\n 2, \n 2.txt\n 3]')
        elif idx_3[-1] > idx_1[-1] > idx_2[-1]:
            print(f'[2.txt\n 1, \n 1.txt\n 2, \n 3.txt\n 3]')
        elif idx_1[-1] > idx_3[-1] > idx_2[-1]:
            print(f'[2.txt\n 1, \n 3.txt\n 2, \n 1.txt\n 3]')
        elif idx_2[-1] > idx_3[-1] > idx_1[-1]:
            print(f'[1.txt\n 1, \n 3.txt\n 2, \n 2.txt\n 3]')
        else:
            print(f'[1.txt\n 1, \n 2.txt\n 2, \n 3.txt\n 3]')

    with open ('res.txt', "w") as f:
        f.write('k')

