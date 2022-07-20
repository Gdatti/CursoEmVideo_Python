def leiaInt(frase):
    n = input(frase)

    while n.isnumeric() is False:
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[0;0m')
        n = input(frase)

    return n


#Main()
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
