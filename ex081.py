lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if q == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 NÃO foi encontrado na lista')

