import math
n = int(input('Digite um número inteiro: '))
opcao = int(input("""Em que você quer converter esse valor? 
1 - Binário, 
2 - Octal ou 
3 - Hexadecimal?
 Digite o número referente a sua escolha: """))
if opcao == 1:
    print('Binário: {}'.format(bin(n)[2:]))
elif opcao == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif opcao == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))