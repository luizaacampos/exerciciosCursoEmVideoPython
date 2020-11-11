
s = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        s += i
print('A soma de todos os valores impares e múltiplos de 3 entre 1 e 500 é {}'.format(s))
