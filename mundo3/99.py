from time import sleep

def maior(*num):
    maior = contador = 0
    print('-=' * 30)
    print('Analisando os valores passados...')

    for v in num:
        if contador == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        contador += 1

        print(f'{v}', end=' ', flush=True)
        sleep(0.5)

    print(f'Foram informados {len(num)} valor(es) ao todo')
    print(f'O maior valor informado foi {maior}')


#Main()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(-6)
maior()
