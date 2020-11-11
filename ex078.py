valores = []
mai = 0
men = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        mai = men = valores[i]
    else:
        if valores[i] > mai:
            mai = valores[i]
        if valores[i] < men:
            men = valores[i]
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}, ', end='')
print(f'\nO menor valor foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}, ', end='')




