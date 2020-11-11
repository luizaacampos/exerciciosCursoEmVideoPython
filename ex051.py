i = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = i + (10 - 1) * r
for c in range(i, decimo + r, r):
    print('{} '.format(c), end='-> ')
print('acabou')
