from random import randint
computador = randint(0, 5)
jogador = int(input("Vou pensar emum numero de 0 a 5, tente adivinhar: "))
if jogador == computador:
    print('Parabéns, você adivinhou! Eu pensei no número {}'.format(computador))
else:
    print('Não foi dessa vez! eu pensei no número {}!'.format(computador))