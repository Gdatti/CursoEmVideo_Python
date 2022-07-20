def notas(*num, sit=False):
    controle = {}

    controle['Total'] = len(num)
    controle['Maior'] = max(num)
    controle['Menor'] = min(num)
    controle['Média'] = sum(num) / len(num)

    if sit is True:
        if controle['Média'] >= 7:
            controle['Situação'] = 'BOA'
        elif controle['Média'] >= 5:
            controle['Situação'] = 'RAZOAVEL'
        else:
            controle['Situação'] = 'RUIM'

    return controle


#Main()
resp = notas(3, 4, 6, 7, 2, 1, 8, 6, sit=True)
print(resp)
