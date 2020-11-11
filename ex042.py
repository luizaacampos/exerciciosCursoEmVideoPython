l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))
if l1 < l2 + l3 and l2 < l1 +l3 and l3 < l1 + l2:
    print('Os segmentos podem formar um triangulo ', end='')
    if l1 == l2 == l3:
        print('EQUILATERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos não podem formar um triangulo')