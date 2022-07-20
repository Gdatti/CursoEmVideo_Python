def leiaDinheiro(frase):
    n = input(frase).replace(',', '.').strip()

    while True:
        try:
            float(n)
            break
        except ValueError:
            print(f'\033[1;31mERRO "{n}" é invalido! Digite somente um valor numerico.\033[0;0m')
            n = input(frase).replace(',', '.').strip()

    return float(n)
