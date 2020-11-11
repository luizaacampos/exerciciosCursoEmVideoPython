lista = []
dado = []
pmax = pmin = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(lista) == 0:
        pmax = pmin = dado[1]
    else:
        if dado[1] > pmax:
            pmax = dado[1]
        if dado[1] < pmin:
            pmin = dado[1]
    lista.append(dado[:])
    dado.clear()
    q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if q == 'N':
        break
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {pmax}kg, peso de ', end='')
for p in lista:
    if p[1] == pmax:
        print(f'[{p[0]}] ', end='')
        p[1] = pmax
print(f'\nO menor peso foi de {pmin}kg, peso de ', end='')
for p in lista:
    if p[1] == pmin:
        print(f'[{p[0]}]', end='')