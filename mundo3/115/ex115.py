from time import sleep
import utilidades
import arqv


#Main()

#Try to open the file and create if needeed
base = 'base.txt'

if arqv.verificaArquivo(base) is False:
    arqv.criaArquivo(base)

while True:
    #Print Menu
    resp = utilidades.menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])

    #Visualizar
    if resp == 1:
            arqv.lerArquivo('base.txt')
    #Cadastrar
    elif resp == 2:
            utilidades.titulo('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = utilidades.leiaInt('Idade: ')
            arqv.cadastrar(base, nome, idade)
    #Sistem Exit
    elif resp == 3:
        utilidades.titulo('Encerrando o Sistema...')
        sleep(1)
        print(f'\033[1;34mSistema Encerrado! Volte Sempre...\033[0;0m')
        break
    else:
        print('\033[1;31mDigite uma opção válida\033[0;0m')
