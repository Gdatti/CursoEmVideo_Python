def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (Opicional) mostra ou n o calculo.
    :return: Retorna o fatorial de N.
    """

    print('-' * 30)
    fat = 1

    for c in range(n, 0, -1):
        fat *= c
        if show is True:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')

    return fat


#Main()
print(fatorial(5, True))
#help(fatorial)
