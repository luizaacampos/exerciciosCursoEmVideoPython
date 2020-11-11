from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua vez de jogar! Digite
0 - Pedra;
1 - Papel;
2 - Tesoura''')
jogador = int(input('Qual será sua jogada? '))
print('Jogador escolheu {}'.format(itens[jogador]))
print('Computador escolheu {}'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('Ninguém ganhou!')
    elif jogador == 1:
        print('Jogador GANHOU!!')
    elif jogador == 2:
        print('Computador GANHOU!!')
elif computador == 1:
    if jogador == 0:
        print('Computador GANHOU!!')
    elif jogador == 1:
        print('Ninguém ganhou!')
    elif jogador == 2:
        print('Jogador GANHOU!!')
elif computador == 2:
    if jogador == 0:
        print('Jogador GANHOU!!')
    elif jogador == 1:
         print('Computador GANHOU!!')
    elif jogador == 2:
        print('Niguém ganhou!!')
else:
    print('Jogada INVÁLIDA!')
