n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior número!'.format(n1))
    if n2<n3:
        print('E {} é o menor número!'.format(n2))
    else:
        print('E {} é o menor número!'.format(n3))
elif n2>n1 and n2>n3:
    print('{} é o maior número!'.format(n2))
    if n1<n3:
        print('e {} é o menor número!'.format(n1))
    else:
        print('e {} é o menor número!'.format(n3))
elif n3>n1 and n3>n2:
    print('{} é o maior número!'.format(n3))
    if n1<n2:
        print('e {} é o menor número!'.format(n1))
    else:
        print('e {} é o menor npúmero!'.format(n2))