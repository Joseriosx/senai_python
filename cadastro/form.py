from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from pessoa import Pessoa

pessoasList = []

def formPessoaFisica():
    nome = input('Informe o nome do cliente: ')
    telefone = input("Informe o telefone do cliente: ")
    cpf = input('Informe o CPF do cliente: ')
    pessoa = PessoaFisica(nome,telefone,cpf)
    addPessoaList(pessoa)

def formPessoaJuridica():
    nome = input('Informe a Razão Social do cliente: ')
    telefone = input("Informe o telefone do cliente: ")
    cnpj = input('Informe o CNPJ do cliente: ')
    pessoa = PessoaJuridica(nome,telefone,cnpj)
    addPessoaList(pessoa)


def addPessoaList(pessoa: Pessoa):
    pessoasList.append(pessoa)

def carregarPessoaCadastrada():
    if not pessoasList:
        print('Nenhum cliente cadastrado')
        return
    
    for pessoa in pessoasList:
        return pessoa.exibir_dados()