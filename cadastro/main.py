from pessoaFisica import PessoaFisica 
from pessoaJuridica import PessoaJuridica

def main():

    list = [] #Para armazenar pessoas
    loop = True

    while loop:
        
        escolha = int(input('1 - Novo cliente | 2 - Listar cliente | 3 - Buscar cliente \n'))
        match escolha:
            case 1:
                tipoCliente = int(input('Deseja cadastrar: \n1 - Pessoa Física | 2 - Pessoa Jurídica \n'))

                if tipoCliente == 1:
                    nome = input('Informe o nome do cliente: ')
                    telefone = input("Informe o telefone do cliente: ")
                    cpf = input('Informe seu cpf: ')
                    cliente = PessoaFisica(nome=nome,telefone=telefone,cpf=cpf)
                    list.append(cliente)
                    print('Cliente registrado com sucesso!')
                else: 
                    nome = input('Informe a Razão Social: ')
                    telefone = input('Informe o telefone: ')
                    cnpj = input('Informe o CNPJ do cliente: ')
                    cliente = PessoaJuridica(nome=nome,telefone=telefone,cnpj=cnpj)
                    list.append(cliente)
                    print('Cliente registrado com sucesso!')

            case 2:
                print('Listar clientes')
            case 3:
                print('Buscar cliente')
            case _:
                print('Inválido')

        opcao = int(input('Deseja continuar o sistema? 1 - Sim | 2 - Não'))
        
        if opcao == 2:
            loop = False


if __name__ == '__main__':
    main()