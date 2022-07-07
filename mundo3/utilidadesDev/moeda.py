def metade(valor=0, formata=False):
    resultado = valor / 2
    if formata is True:
        return moeda(resultado)
    return resultado

def dobro(valor=0, formata=False):
    resultado = valor * 2
    if formata is True:
        return moeda(resultado)
    return resultado

def aumentar(valor=0, taxa=0, formata=False):
    resultado = valor + (valor * (taxa/100))
    if formata is True:
        return moeda(resultado)
    return resultado

def diminuir(valor=0, taxa=0, formata=False):
    resultado = valor - (valor * (taxa/100))
    if formata is True:
        return moeda(resultado)
    return resultado

def moeda(valor=0, tipo='R$'):
    return (f'{tipo}{valor:.2f}').replace('.', ',')

def resumo(valor=0, aumento=0, redução=0):
    print('-' * 32)
    print(f'{"RESUMO DO VALOR":^32}')
    print('-' * 32)

    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço:\t{metade(valor, True)}')
    print(f'{aumento}% de aumento:\t\t{aumentar(valor, aumento, True)}')
    print(f'{redução}% de redução:\t\t{diminuir(valor, redução, True)}')

    print('-' * 32)
