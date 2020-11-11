from random import randint
from time import sleep
mega = []
jogos = []
quant = int(input('Quantos jogos vocêquer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    tot += 1
print('-='*3, f' Sorteando {quant} jogos ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
