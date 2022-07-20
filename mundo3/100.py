from random import randint
from time import sleep

números = []

def sorteia():
    print('Sorteando os 5 valores da lista: ', end='')

    for c in range(0, 5):
        n = randint(1, 10)
        números.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)

    print('PRONTO!')


def somaPar(lst):
    pares = 0
    for v in lst:
        if v % 2 == 0:
            pares += v

    print(f'Somando os valores pares de: {lst}, temos: {pares}')


#Main()
sorteia()
somaPar(números)
