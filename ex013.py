salario = float(input('Qual é o salario do funcionário? R$'))
novo_salario = salario * 1.15
print('Um funcionário que recebia R${:.2f}, com 15% de aumento passa a receber R%{:.2f}'.format(salario, novo_salario))