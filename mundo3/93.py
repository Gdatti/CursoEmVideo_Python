jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}?: ')))
jogador['Gols'] = gols.copy() #[:]
jogador['Total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for campos in jogador: #items()
    print(f'O campo: {campos} tem o valor: {jogador[campos]}')

print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
