from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho: (0 se não possuir) '))
if dados['CTPS'] != 0:
    dados['contratação'] =int(input('ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-'*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')