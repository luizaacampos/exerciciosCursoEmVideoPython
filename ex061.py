pt = int(input('1º Termo: '))
r = int(input('Razão: '))
t = pt
cont = 1
while cont <= 10:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1
print('FIM')