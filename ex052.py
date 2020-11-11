n1 = int(input('Digite um número: '))
tot = 0
for i in range(1, n1 + 1):
    if n1 % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n1, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
