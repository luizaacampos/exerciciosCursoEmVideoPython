'''n = 0
cont = 0
som = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    som += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, som - 999))
'''
############# OU ####################

n = cont = som = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    som += n
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, som))

#o flag (999) não é add pois o loop é encerrado antes 