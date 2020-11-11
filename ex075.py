num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O primeiro valor 3 foi digitado na posição {num.index(3)}')
print('Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(f'{c}, ', end='')