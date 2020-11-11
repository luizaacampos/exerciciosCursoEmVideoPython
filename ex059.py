from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Qual é sua opção? '''))
    if opcao == 1:
        print('A soma é {}'.format(n1+n2))
    elif opcao == 2:
        print('A multiplicação é {}'.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior'.format(n1))
        else:
            print('{} é maior'.format(n2))
    elif opcao == 4:
        print('Informe os novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Código inválido')
    print('=-='*10)
    sleep(1)
print('Fim do programa, volte sempre!')
