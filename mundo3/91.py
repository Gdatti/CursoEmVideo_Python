from random import randint
from time import sleep

jogadas = {}
contador = 1

for c in range(1, 5):
    jogadas[f'Jogador{c}'] = randint(1, 6)

print(' ->Valores sorteados:')
for jogador in jogadas:
    print(f'   O {jogador} tirou {jogadas[jogador]} no dado.')
    sleep(1)

print('-=' * 20)
print(' ->Ranking dos jogadores:')
for c in sorted(jogadas, key = jogadas.get):
    print(f'   {contador}º lugar {c}: com {jogadas[c]} no dado.')
    contador += 1
    sleep(1)
