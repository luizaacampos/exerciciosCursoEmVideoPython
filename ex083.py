n = str(input('Digite uma expressão matemática: '))
pilha = []
for simb in n:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')