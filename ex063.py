print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
pt = 0
st = 1
print('{} -> {} '.format(pt, st), end='')
cont = 3
while cont <= n:
    tt = pt + st
    print(' -> {}'.format(tt), end='')
    pt = st
    st = tt
    cont += 1
print(' -> FIM')


