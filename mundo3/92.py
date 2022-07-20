from datetime import date

ano = date.today().year
dados = {}

dados['Nome'] = str(input('Nome: '))

nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = ano - nascimento

dados['Ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salários: '))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (ano - (dados['Contratação'])))

    print('-=' * 30)
    print(dados)
    for info in dados:
        print(f'{info} tem o valor: {dados[info]}')

else:
    print('-=' * 30)
    print(dados)
    for info in dados:
        print(f'{info} tem o valor: {dados[info]}')
