tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre zero e 20: '))
if n > 20:
    print('Tente novamente! ', end='')
    n = int(input('Digite um número entre zero e 20: '))
print(f'Você digitou o número {tupla[n]}')