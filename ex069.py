cont18 = contH = contM20 = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contH += 1
    if sexo == 'F' and idade < 20:
        contM20 += 1
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {contH} homens cadastrados')
print(f'E temos {contM20} mulheres com menos de 20 anos')
