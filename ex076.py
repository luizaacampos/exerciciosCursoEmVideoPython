listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno',15.90,
            'Penal', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)

#:^40 -> com 40 caracteres, centralizado
#:30 -> print com 30 caracteres
#:.<30 -> com 30 caracteres, alinhado a esquerda e cheio de .
#:>7 -> com 7 caracteres, alinhado a direita
#:>7.2f -> com 7 caracteres, alinhado a direita e com 2 casas decimais