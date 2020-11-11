aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] =float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Em recuperação'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
