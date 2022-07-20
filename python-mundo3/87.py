lista = [[],[],[]]
pares = 0
terceira = 0

for c in range(0, 3):
    for l in range(0, 3):
        lista[c].append(int(input(f'Digigite um valor para a posição [{c} : {l}]: ')))

print('-=' * 20)

for c in range(0, 3):
    for l in range(0, 3):
        if lista[l][c] % 2 == 0:
            pares += lista[l][c]

        print(f'[ {lista[c][l]} ]', end='')
    print()

print('-=' * 20)
print(f'A soma dos valores PARES é {pares}.')

for numeros in lista:
    terceira += numeros[2]

print(f'A soma da TERCEIRA coluna é {terceira}')
print(f'O maior valor da segunda LINHA é {max(lista[1])}')
