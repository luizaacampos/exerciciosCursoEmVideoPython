jogador = dict()
partidas = list()
#pergunta nome do jogador
jogador['nome'] = str(input('Nome do jogador: '))

#pergunta quantas partidas jogou
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#pergunta quantos gols a cada partida
for i in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {i}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   Na partida {i}, fez {v} gols.')
print(f'Fez um total de {jogador["total"]} gols')

#guarda tudo em um dicionario, incluindo total de gols