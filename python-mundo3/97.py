def titulo(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)


#Main()
titulo('Guilherme Datti')
titulo('Acorda Pedrinho')
titulo('GG')

texto1 = str(input('Digite um titulo: '))
titulo(texto1)
