casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salario? R$'))
anos = int(input('você quer pagar em quantos anos? '))
mensal = casa / (anos * 12)
minimo = salario * 0.30
if mensal <= minimo:
    print('Para pagar umacasa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
    print('A prestação será de R${:.2f}. Empréstimo concedido!'.format(mensal))
else:
    print('Desculpa, mas seu impréstimo não foi aprovado')
