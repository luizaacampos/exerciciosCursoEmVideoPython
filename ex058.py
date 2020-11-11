from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = 0
tentativas = 0
while jogador != computador:
    jogador = int(input('Qual é seu palpite? '))
    if jogador < computador:
        print('Mais... Tente mais uma vez')
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

#guanabara
''' from rand....
computador...
print('Sou.....
acertou = False
palpites = 0
while not acertou:
    jogador = int.....
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...
        elif jogador > computador:
            print('Menos....
print('Acertou com....'''
