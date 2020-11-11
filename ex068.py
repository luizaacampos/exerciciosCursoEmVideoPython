from random import randint
cont = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Jogue um numero: '))
    soma = computador + jogador
    tipo = str(input('par ou impar [P/I]? ')).upper().strip()[0]
    print(f'{computador} mais {jogador} dá {soma} ', end='')
    if soma % 2 == 0:
        print('Deu PAR')
        if tipo in 'Pp':
            print('Você VENCEU')
            #cont += 1
        else:
            print('VocÊ PERDEU')
            break
    if soma % 2 != 0:
         print('Deu IMPAR')
         if tipo in 'Ii':
             print('Você VENCEU')
             #cont += 1
         else:
             print('Você PERDEU')
             break
    cont += 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes')
