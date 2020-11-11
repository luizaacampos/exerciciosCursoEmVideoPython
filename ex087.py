matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
maior2l = somacol3 = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somapares}')
for l in range(0, 3):
    somacol3 += matriz[l][2]
#somacol3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna foi de {somacol3}')
'''
if matriz[1][0] > maior2l:
    maior2l = matriz[1][0]
if matriz[1][1] > maior2l:
    maior2l = matriz[1][1]
if matriz[1][2] > maior2l:
    maior2l = matriz[1][2]
'''
for c in range(0, 3):
    if c == 0:
        maior2l = matriz[1][c]
    elif matriz[1][c] > maior2l:
        maior2l = matriz[1][c]
print(f'O maior valor da segunda linha é {maior2l}')
