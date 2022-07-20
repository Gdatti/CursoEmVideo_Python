def voto(ano):
    from datetime import date

    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')

    if idade < 16:
        return 'NÃO VOTA!'
    elif 16 <= idade < 18 or idade >= 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATORIO!'


#Main()
nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(nascimento))
