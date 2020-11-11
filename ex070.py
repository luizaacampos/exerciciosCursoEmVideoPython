total = tk = menor = soma = 0
print('--------------Loja Sallus-----------------')
while True:
    prod = input('Nome do produto: ')
    valor = float(input('Preço: R$'))
    soma += 1
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    total += valor
    if valor > 1000.00:
        tk += 1
    if soma == 1 or valor < menor:
        menor = valor
        barato = prod
    if cont == 'N':
        break
print('---------FIM DO PROGRAMA-------------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {tk} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

