r1 = float(input('Primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima NÃO podem formar um triangulo!')