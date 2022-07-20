from time import sleep

lista = []

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[:1]

    lista.append([nome, [nota1, nota2]])

    while True:
        if continuar not in 'SN':
            continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[:1]
        else:
            break

    if continuar in 'N':
        break

print('-=' * 16)
print(f'{"No.":<5}{"NOME":<10}{"MEDIA":>12}')
print('-' * 27)

for i, name in enumerate(lista):
    sleep(0.25)
    print(f'{i:<5}{name[0]:<10}{(sum(name[1])/2):>12.2f}')
    sleep(0.25)

print('-' * 27)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    while True:
        if mostrar not in range(0, len(lista)) and mostrar != 999:
            mostrar = int(input('Opcao invalida...Mostrar notas de qual aluno? (999 interrompe): '))
        else:
            break

    if mostrar == 999:
        print('-' * 27)
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print('-' * 27)
        print(f'As notas de {lista[mostrar][0]} sao: {lista[mostrar][1]}')
        print('-' * 27)
