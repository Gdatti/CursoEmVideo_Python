from time import sleep

cores = ('\033[m',         #0 - Reset
         '\033[0;30;41m',  #1 - Vermelho
         '\033[0;30;43m',  #2 - Amarelo
         '\033[7;30m',     #3 - Branco
         )

def ajuda(comando):
    print(titulo(f'Procurando o documento de {comando}...', 2))
    sleep(1)
    help(comando)


def titulo(msg, c=0):
    tam = len(msg) + 4
    print(cores[c], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')

#Main()
while True:
    duvida = str(input('Comando > ')).strip()
    if duvida.upper() == 'FIM':
        break
    ajuda(duvida)
titulo('Volte sempre!', 1)
