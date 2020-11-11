vel = int(input("Qual a velocidade do carro? "))
if vel > 80:
    print('você está acima da velocidade!')
    print('Sua multa vai custar {} reais'.format(((vel-80)*7)))
else:
    print("Você está sentro da velocidade permitida!")