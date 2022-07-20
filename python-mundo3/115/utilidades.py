cor = ('\033[0;0m',    #0 - Reset
       '\033[;1m',     #1 - Negrito
       '\033[1;34m',   #2 - Azul
       '\033[1;31m',   #3 - Vermelho
       '\033[1;33m',   #4 - Amarelo
       '\033[1;92m',   #5 - Verde
       )


def menu(lista):
    titulo('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'{cor[4]}{i + 1}{cor[2]} - {v}{cor[0]}')
    print('-' * 60)

    menu = leiaInt(f'{cor[5]}Sua Opção:{cor[0]} ')
    return menu


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;91mErro: Pfvr, digite um número Inteiro Válido.\033[0;0m')
        except KeyboardInterrupt:
            print(f'\033[1;91m\nErro: Usuário preferiu não digitar esse número.\033[0;0m')
            return 0
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;91mErro: Pfvr, digite um número Inteiro Válido.\033[0;0m')
        except KeyboardInterrupt:
            print(f'\033[1;91m\nUsuário preferiu não digitar esse número.\033[0;0m')
            return 0
        else:
            return valor


def titulo(msg):
    print('-' * 60)
    print(f'{msg:^60}')
    print('-' * 60)
