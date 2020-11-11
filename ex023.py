num = int(input('Informe um número: '))
#print('Unidade: {}'.format(num[-1]))
#print('Dezena: {}'.format(num[-2]))
#print('Centena: {}'.format(num[-3]))
#print('Milhar: {}'.format(num[-4]))

u = num // 1 % 10
d = num //10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
