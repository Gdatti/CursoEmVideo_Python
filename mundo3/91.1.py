from random import randint
from time import sleep
from operator import itemgetter

jogadas = {}
ranking = {}

for c in range(1, 5):
    jogadas[f'Jogador{c}'] = randint(1, 6)

print(' ->Valores sorteados:')
for k, v in jogadas.items():
    print(f'   O {k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('-=' * 20)
print(' ->Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar {v[0]}: com {v[1]} no dado.')
    sleep(1)
