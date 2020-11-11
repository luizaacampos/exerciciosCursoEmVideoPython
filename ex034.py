salario = float(input('Qualo salário do funcionario? '))
if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
    print('Seu novo salário é de R${:.2f}'.format(novo_salario))
else:
    novo_salario2 = salario + (salario*0.10)
    print('Seu novo salárioé de R${:.2f}'.format(novo_salario2))