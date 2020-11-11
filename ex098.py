from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'\ncontagem de {i} até {f} em {p}')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p


contador(1, 10, 1)
contador(10, 0, 2)
print('\nAgora é sua vez!')
ini = int(input('inicio: '))
fim = int(input('fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)