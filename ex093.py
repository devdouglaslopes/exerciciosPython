jogador = {}
gols = []
tot_gols = 0
nome_jogador = str(input('Nome do jogador: '))
jogador['nome'] = nome_jogador
partidas = int(input('Quantidade de partidas: '))
jogador['partidas'] = partidas
for p in range(1, partidas+1):
    gols_pt = int(input(f'Quantidade de gols da partida {p}: '))
    tot_gols += gols_pt
    gols.append(gols_pt)
jogador['gols'] = gols
jogador['total de gols'] = tot_gols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {nome_jogador} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'   => Na partida {i+1}, fez {gols[i]} gols')
print(f'Foi um total de {tot_gols} gols.')