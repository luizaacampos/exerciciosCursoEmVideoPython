#num = float(input('Digite um numero: '))
#num_int = int(num)
#print('o numero {} tem a parte inteira {}'.format(num, num_int))

from math import trunc
num = float(input('Digite um numero: '))
print('o numero {} tem a parte inteira {}'.format(num, trunc(num)))