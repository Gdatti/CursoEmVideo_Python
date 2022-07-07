import utilidades


cor = ('\033[0;0m',    #0 - Reset
       '\033[;1m',     #1 - Negrito
       '\033[1;34m',   #2 - Azul
       '\033[1;31m',   #3 - Vermelho
       '\033[1;33m',   #4 - Amarelo
       '\033[1;92m',   #5 - Verde
       )


def verificaArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except:
        print('Erro ao tentar abrir o arquivo.')
        return False
    else:
        print('Arquivo aberto com sucesso.')
        return True


def criaArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        utilidades.titulo('PESSOAS CADASTRADAS')
        for linha in arquivo:
            info = linha.split(';')
            info[1] = info[1].replace('\n', '')
            print(f'{info[0]:<50}{info[1]} anos')
    finally:
        arquivo.close()


def cadastrar(arquivo, nome, idade):
    try:
        ar = open(arquivo, 'at')
    except:
        print('Erro ao tentar abrir o arquivo.')
    else:
        try:
            ar.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados no arquivo.')
        else:
            print('-' * 60)
            print(f'{cor[5]}Novo registro de {nome} adicionado com sucesso.{cor[0]}')
            ar.close()
