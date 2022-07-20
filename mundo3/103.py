def ficha(nome, gols):
    print('-' * 30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonado.')


#Main()
print('-' * 30)
n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de gols: ')).strip()

if g.isnumeric():
    g = int(g)
else:
    g =0

if n == '':
    n = 'Desconhecido'

ficha(n, g)
