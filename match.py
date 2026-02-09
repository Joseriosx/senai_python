categoria = int(input('Informe uma categoria: '))
qtd = int(input('Informe uma quantidade: '))
valor = 0
error = False

match categoria:
    case 1:
        valor = 10.
    case 2:
        valor = 18.
    case 3:
        valor = 23.
    case 4:
        valor = 26.
    case 5:
        valor = 31.
    case _:
        error = True
        print('Categoria inválida, digite um valor de 1 a 5.')

if not error :
    print(f'Categoria {categoria}\nPreço unitário: {valor}\nQuantidade: {qtd}\nTotal: {valor * qtd}')
