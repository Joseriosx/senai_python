categoria = int(input('Informe uma categoria: '))
qtd = int(input('Informe uma quantidade: '))
valor = 0


if categoria == 1:
    valor = 10.0
elif categoria == 2:
    valor = 18.
elif categoria == 3:
    valor = 23.
elif categoria == 4:
    valor = 26.
elif categoria == 5:
    valor = 31.
else:
    error = True
    print('Categoria inválida, digite um valor de 1 a 5.')

if not error:
    print(f'Categoria {categoria}\nPreço unitário: {valor}\nQuantidade: {qtd}\nTotal: {valor * qtd}')