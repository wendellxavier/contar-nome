nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'seu nome é curto, ele tem {tamanho} letras')
elif tamanho <= 6:
    print(f'seu nome tem tamanho normal, ele tem {tamanho} de letras')
else:
    print(f'seu nome é muito grande, ele tem {tamanho} letras')