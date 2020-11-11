import random
aluno_1 = input('Digite o nome do primeiro aluno: ')
aluno_2 = input('Digite o nome do segundo aluno: ')
aluno_3 = input('Digite o nome do terceiro aluno: ')
aluno_4 = input('Digite o nome do quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = random.choice(lista)
print('O escolhido foi {}!'.format(escolhido))
