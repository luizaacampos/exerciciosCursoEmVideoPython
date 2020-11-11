import math
b2 = float(input('Qual o comprimento do cateto oposto: '))
c2 =float(input('Qual o comprimento do cateto adjacente: '))
#a = sqrt((b2 * b2) + (c2 * c2))
#a = (b2 ** 2 + c2 ** 2) ** 1/2
a = math.hypot(b2, c2)
print('A hipotenusa vai medir {:.2f}'.format(a))