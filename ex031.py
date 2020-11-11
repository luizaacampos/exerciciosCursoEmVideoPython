km = int(input('Qual a distancia rm km a ser viajada? '))
if km <= 200:
    print('O custo da viagem será de R${:.2f}'.format(km*0.50))
else:
    print('O custo da viagem será de R${:.2f}'.format(km*0.45))