continuar = True
frutas = {}

while continuar:

    print(f'Selecione as opções abaixo: \n1 - Add | 2 - Remover | 3 - Buscar')

    opcao = int(input('Informe a opção: '))
    nome_fruta = ''
    valor_fruta = 0.0

    match opcao:
        case 1: 
            nome_fruta = input('Informe o nome da Fruta: ')
            valor_fruta = float(input('Informe o preço da Fruta: '))
            frutas.update({
                nome_fruta: valor_fruta
            })
        
        case 2:
            nome_fruta = input('Informe o nome da fruta: ')
            del frutas[nome_fruta]

            print(f'A fruta removida foi {nome_fruta}')

        case 3:
            nome_fruta = input('Informe o nome para busca:')
            print(f'{frutas[nome_fruta]}')

        case _:
            print('Opção inválida')

    opcao = int(input('Deseja continuar cadastrando? 1-sim | 2-não \n'))

    if opcao == 2:
        continuar = False
print('Encerrando aplicação')

print(f'Imprimindo as frutas: \n{frutas}')