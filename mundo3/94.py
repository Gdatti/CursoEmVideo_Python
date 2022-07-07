lista = []
pessoa = {}
idadetotal = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()

    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[:1]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')

    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())

    while True:
        continuar = str(input('Deseja continuar [S/N]?: ')).upper().strip()[:1]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if continuar in 'N':
        break

print('-=' * 30)
print(f'- O grupo tem {len(lista)} pessoas.')

for indice, dicio in enumerate(lista):
    idadetotal += lista[indice]['Idade']

media = idadetotal / len(lista)
print(f'- A média de idade é de: {media:.2f} anos.')

print('- As mulheres cadastradas foram: ',end='')
for people in lista:
    if people['Sexo'] in 'Ff':
        print(f'{people["Nome"]}', end=' ')
print()

print(f'- Lista de pessoas que estão acima da médida de idade: ')
for indice, dicio in enumerate(lista):
    if lista[indice]['Idade'] > media:
        print(f'\nNome = {lista[indice]["Nome"]}; Sexo = {lista[indice]["Sexo"]}; Idade = {lista[indice]["Idade"]}')
