dados = []

def registrar(nome='', idade=0):

    dados.append({nome, idade})

    with open('dados.txt', 'w') as arquivo:
        arquivo.write(str(dados))
        arquivo.close()
    print(f'Novo registro de {nome} adicionado!')
