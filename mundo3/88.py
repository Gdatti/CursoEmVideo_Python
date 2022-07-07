from random import randint
from time import sleep

quantidade = int(input('Quantos jogos da LOTERIA você quer que fazer?: '))

jogos = []
temp = []
contador = 1

print()
print('-=' * 4, end=' ')
print('Sorteando', end=' ')
print(f'{quantidade}', end=' ')
print('Jogos', end=' ')
print('-=' * 4)

for i in range(0, quantidade):
    while contador <= 6:
        aleatorio = randint(1, 60)
        if aleatorio not in temp:
            temp.append(aleatorio)
            contador += 1
    contador = 1

    jogos.append(temp[:])
    temp.clear()

    sleep(0.5)
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(0.5)

print('-=' * 6, end=' ')
print('BOA SORTE', end=' ')
print('-=' * 6)
