lista = []
temp = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    continuar = str(input('Deseja continuar [S/N]?: ')).upper().strip()[:1]

    lista.append(temp[:])
    temp.clear()

    while True:
        if continuar not in 'SN':
            continuar = str(input('Deseja continuar [S/N]?: ')).upper().strip()[:1]
        else:
            break

    if continuar in 'N':
        break

print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {(max(lista)[1])}, peso de: ', end='')

for p in lista:
    if p[1] == (max(lista)[1]):
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso foi de {(min(lista)[1])}, peso de: ', end='')

for p in lista:
    if p[1] == (min(lista)[1]):
        print(f'{p[0]}', end=' ')

print()
