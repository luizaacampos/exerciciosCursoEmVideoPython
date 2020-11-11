ano = int(input('Ano de nascimento: '))
idade = 2020 - ano
falta = 18 - idade
passou = idade - 18
print('Quem nasceu em {} tem {} anos em 2020.'.format(ano, idade))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(falta))
    print('Se alistamento será em {}.'.format(2020 + falta))
elif idade >= 18:
    print('Você já devia ter se alistado há {} anos.'.format(passou))
    print('Seu alistamento foi em {}.'.format(2020 - passou))