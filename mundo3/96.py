def area(larg, compr):
    area = larg * compr
    print(f'A area do seu terreno ({larg} x {compr}) eh de: {area} m².')


#Main()
print('-' * 20)
print('Controle de Terrenos')
print('-' * 20)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)
