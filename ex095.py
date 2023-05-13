jogadores = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot_partidas = int(input('Quantidade de partidas: '))
    partidas.clear()
    for p in range(1, tot_partidas+1):
        partidas.append(int(input(f'Quantidade de gols da partida {p}: ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    jogadores.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('-=' * 20)
print(f'{"cod":>3} ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(jogadores):
    print(f'{i:>3} ', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
opcao = 0
while opcao != 999:
    opcao = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if opcao == 999:
        break
    if opcao >= len(jogadores):
        print(f'Error! Não existe jogador com código {opcao}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}')
        for i, j in enumerate(jogadores[opcao]['gols']):
            print(f'Na partida {i+1} fez {j} gols.')
print(' <<< Volte Sempre >>> ')