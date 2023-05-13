times = [' ','Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude']
print(f'Os primeiros 5 colocados são {times[1:6]}')
print(f'Os ultimos 4 colocados são {times[-4:]}')
print(f'A lista dos times em ordem alfabética: {sorted(times)}')
time_c = 'Corinthians'
print(f'O time Corinthians está na posição {times.index(time_c)}')