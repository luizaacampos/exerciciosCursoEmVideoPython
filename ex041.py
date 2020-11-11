ano = int(input('Digite o ano do seu nascimento: '))
idade = 2020 - ano
if idade <= 9:
    print('Você possui {} anos e se encaixa na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você possui {} anos e se encaixa na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você possui {} anos e se encaixa na categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Você possui {} anos e se encaixa na categoria SENIOR'. format(idade))
else:
    print('Você possui {} anos e se encaixa na categoria MASTER'.format(idade))


