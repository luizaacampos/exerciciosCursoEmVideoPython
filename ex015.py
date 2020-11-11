dias = int(input('Você alugou o carro por quantos dias? '))
km = float(input('Quantos km foram rodados? '))
preco = (60*dias)+(0.15*km)
print('O preço do aluguel será R${:.2f}'.format(preco))