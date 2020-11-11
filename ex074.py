from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = 0
menor = 10
print(num)
for c in num:
    if c > maior:
        maior = c
    if c <menor:
        menor = c
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

'''
print('Os valores sorteados foram: ', end='')
for n in num:
        print(f'{n}', end='')
print(f'\nOmaior valor sorteado foi {max(num)}')
print(f'Omenor valor sorteado foi {min(num)}')
'''