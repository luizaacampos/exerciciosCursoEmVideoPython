print('***LOJAS SALLUS***')
valor = float(input('Entre com o valor da compra: R$'))
pagamento = int(input("""1 - A vista (dinheiro ou cheque);
2 - a vista no cartão;
3 - Parcelado em até 2x no cartão;
4 - Parcelado em 3x ou mais no cartão.
Escolha o método de pagamento: """))
if pagamento == 1:
    print('O valor da compra atualizado é de R${:.2f}.'.format((valor - (valor*0.1))))
elif pagamento == 2:
    print('O valor atualizado da compra é de R${:.2f}.'.format((valor-(valor*0.05))))
elif pagamento == 3:
    print('Dessa forma você pagará 2 parcelas de R${:.2f}.'.format(valor/2))
elif pagamento == 4:
    parcelas = int(input("Em quantas parcelas você gostaria de fazer? (Até 6): "))
    valor_att = valor + (valor*0.20)
    if parcelas == 3:
        print('Você pagará parcelas de R${:.2f}'.format(valor_att/3))
    elif parcelas == 4:
        print('Você pagará parcelas de R${:.2f}'.format(valor_att / 4))
    elif parcelas == 5:
        print('Você pagará parcelas de R${:.2f}'.format(valor_att / 5))
    elif parcelas == 6:
        print('Você pagará parcelas de R${:.2f}'.format(valor_att / 6))
else:
     print('Valor inválido!')