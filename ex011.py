l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
t = a * 0.5
print('Sua parede tem dimensão de {}X{} e sua area é de {}m².\n Para pintar essa parede você vai precisar de {}litros de tinta.'.format(l, h, a, t))