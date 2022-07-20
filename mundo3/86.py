lista = [[],[],[]]

for c in range(0, 3):
    for l in range(0, 3):
        lista[c].append(int(input(f'Digite um valor para a posição [{c}, {l}]: ')))

print('-=' * 15)

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {lista[c][l]} ]', end='')
    print()
