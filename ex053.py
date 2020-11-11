frase = input('Escreva uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto)
print(inverso)
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palindromo')