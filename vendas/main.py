from cliente import Cliente
from produto import Produto
from venda import Venda

def menu():
    print('\n' + '='*30)
    print('      Sistemas de Vendas')
    print('='*30)
    print('1. Cadastrar Cliente')
    print('2. Cadastrar Produtos')
    print('3. Realizar Venda')
    print('0. Sair')
    return input('\nEscolha uma opção: ')

def listar_clientes():
    with open('clientes.txt', 'r') as f:
        for linha in f:
            dados = linha.strip().split(';')
            print(f'{dados[0]} - {dados[1]}')

def listar_produtos():
    with open('produtos.txt', 'r') as f:
        for linha in f:
            dados = linha.strip().split(';')
            print(f'{dados[0]} - {dados[1]} - {dados[2]}')             


def main():
    continuar = True

    while continuar:
        opcao = menu()


        match opcao:
            case '1':
                cpf = input('Informe o CPF: \n')  #
                nome = input('Informe o nome: \n')  #
                cliente = Cliente(cpf, nome)   #
                cliente.salvar()   #
                print('Cadastrar cliente')

            case '2':
                codigo = int(input('Informe um código: '))
                descricao = input('Informe nome do produto: ')
                valor = float(input('Informe valor do produto: '))
                produto = Produto(codigo, descricao,valor)
                produto.salvar() 
                print('Cadastrar produto')

            case '3':
                # cadastrar cliente
                cpf = input('Informe o CPF: \n')  
                nome = input('Informe o nome: \n')  
                cliente = Cliente(cpf, nome)   
                cliente.salvar()   

                venda = Venda(cliente)

                addProduto = True

                while addProduto:
                    codigo = int(input('Informe um código: '))
                    descricao = input('Informe nome do produto: ')
                    valor = float(input('Informe valor do produto: '))
                    produto = Produto(codigo, descricao,valor)
                    produto.salvar() 
                    venda.addProdutoVenda(produto)

                    sair = input('deseja adicionar mais produtos? 1 - sim | 2 - não')
                    if int(sair) == 2:
                        addProduto = False

                venda.salvar()



                print('Realizar venda')

            case '0':
                print('Sair do sistema')
                continuar = False

            case _:
                print('Opção inválida')

if __name__ == '__main__':
    main()
            