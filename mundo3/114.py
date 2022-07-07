import webbrowser

site = str("google.com.br")

try:
    webbrowser.open(site)
except:
    print(f'Nao Consegui abrir o site :(')
else:
    print(f'Consegui abrir o site Pudim com sucesso!')
