continuar = True
lista = []

while continuar:
    fruta = input('Informe uma fruta: ')
    lista.append(fruta)

    desejaContinuar = input('Deseja continuar? Sim (s) | Não (n): ')

    if(desejaContinuar.strip().lower() == 'n'):
        continuar = False

print(f'Sua lista de frutas:\n{lista}')