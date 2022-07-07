def leiaInt():
    while True:
        try:
            valor = int(input('Digite um número Inteiro: '))
        except ValueError:
            print(f'\033[1;91mErro: Pfvr, digite um número Inteiro Válido.\033[0;0m')
        except KeyboardInterrupt:
            print(f'\033[1;91m\nUsuário preferiu não digitar esse número.\033[0;0m')
            valor = 0
            return valor
        else:
            return valor


def leiaFloat():
    while True:
        try:
            valor = float(input('Digite um número Real: '))
        except ValueError:
            print(f'\033[1;91mErro: Pfvr, digite um número Inteiro Válido.\033[0;0m')
        except KeyboardInterrupt:
            print(f'\033[1;91m\nUsuário preferiu não digitar esse número.\033[0;0m')
            valor = 0
            return valor
        else:
            return valor


#Main()
i = leiaInt()
r = leiaFloat()
print(f'O valor Inteiro digitado foi {i} e o valor Real foi {r}')
