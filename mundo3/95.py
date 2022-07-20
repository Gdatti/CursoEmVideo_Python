time = []
gols = []
jogador = {}

while True:
    jogador['Nome'] = str(input('Nome do jogador: '))

    partidas = int(input(f'- Quantas partidas {jogador["Nome"]} jogou?: '))
    for i in range(0, partidas):
        gols.append(int(input(f'   *Quantos gol(s) na partida {i + 1}?: ')))
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    gols.clear()

    time.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[:1]
        if continuar in 'SN':
            break
        print('Erro! Digite S ou N para continuar ou não:')

    if continuar in 'N':
        break

print('-=' * 25)
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 50)

for i, v in enumerate(time):
    print(f'{i:<5}{time[i]["Nome"]:<20}{str(time[i]["Gols"]):<22}{time[i]["Total"]}')
print('-' * 50)

while True:
    codigo = int(input('Levantar dados de qual jogador? Digite "999" para encerrar: '))

    if codigo == 999:
        break

    if codigo not in range(0, len(time)):
        print(f'ERRO! Não existe jogador com o código {codigo}! Tente novamente...')
        print('-' * 50)

    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[codigo]["Nome"]}:')
        for i, gol in enumerate(time[codigo]['Gols']):
            print(f'   No jogo {i + 1} fez {gol} gol(s).')
        print('-' * 50)

print('<< VOLTE SEMPRE >>')
