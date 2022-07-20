from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= - 1

    if p == 0:
        p = 1

    print(f'Contagem de {i} ate {f} de {p} em {p}:')

    if i > f and p > 0:
        p *= - 1
    f += p

    for c in range(i, f, p):
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)

    print('FIM!')
    print('-' * 30)


#Main()
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora e a sua vez de personalizar a contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
