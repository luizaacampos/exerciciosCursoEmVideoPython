n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2)/2
if media < 5.0:
    print('Sua média é {:.1f}, você foi REPROVADO!'.format(media))
elif media >= 5.0 and media < 6.9:
    print('Sua média é {:.1f} e você está em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua média é {:.1f} e você foi APROVADO!'.format(media))