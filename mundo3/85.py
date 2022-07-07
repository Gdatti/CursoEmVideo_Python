lista = [[],[]]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1} valor: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Os PARES digitados foram: {sorted(lista[0])}')
print(f'Os IMPARES digitados foram: {sorted(lista[1])}')
