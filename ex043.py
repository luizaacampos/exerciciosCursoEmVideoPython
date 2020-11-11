peso = float(input('Entre com seu peso: '))
altura = float(input('Entre com sua altura em m: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}. Você está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.1f}. Você está no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.1f}. Você está com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.1f}.Você está com obesidade'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Você está com obesidade mórbida.'.format(imc))