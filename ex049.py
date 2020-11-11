c = 1
for i in range(1, 11):
    for c in range(1, 11, 1):
        print('{} x {} = {}'.format(i, c, i*c))

#OU

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))