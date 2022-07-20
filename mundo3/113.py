def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;91mErro: Pfvr, digite um número Inteiro Válido.\033[0;0m')
        except KeyboardInterrupt:
            print(f'\033[1;91m\nUsuário preferiu não digitar esse número.\033[0;0m')
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


#Main()
i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {i} e o valor Real foi {r}')
