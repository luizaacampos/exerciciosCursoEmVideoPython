lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor suplicado... Não vou adicionar!')
    pg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pg == 'N':
        break
print(sorted(lista))
