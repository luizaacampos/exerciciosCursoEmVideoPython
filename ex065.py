cont = soma = n = media = 0
seg = 'S'
while seg in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    seg = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))