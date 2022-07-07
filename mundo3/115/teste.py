import comandos

#Main()
print('-' * 50)
print(f'{"Menu Principal":^50}')

while True:
    print('-' * 50)

    print('''1 - Ver pessoas cadastradas
2 - Cadastar nova pessoa
3 - Sair do Sistema''')
    print('-' * 50)

    op = int(input('Sua Opcao: '))
    if op == 3:
        break
    if op == 2:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        comandos.registrar(nome, idade)
