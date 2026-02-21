from conta import Conta
from pessoa import Pessoa
from corrente import ContaCorrente
from endereco import Endereco
from contato import Contato

def main():

    endereco = Endereco('Rua teresina,1878', 'São João', 'Teresina', 'PI')
    contato1 = Contato('86', '9999-6666')

    maria = Pessoa('Maria Joaquina', endereco)
    mariaConta = ContaCorrente(2, maria)
    mariaConta.depositar(1000)
    maria.add_contato(contato1)

    print(maria.mostrarDados())

    joao = Pessoa('João Henrique', endereco)
    joaoConta = Conta(1, joao)
    joaoConta.depositar(150)

    mariaConta.transferir(100, joaoConta)


    print(mariaConta.visualisarDadosConta())
    print(mariaConta.visualisarSaldoConta())

    #mariaConta.sacar(100)


    print(joaoConta.visualisarDadosConta())
    print(joaoConta.visualisarSaldoConta())

    #joaoConta.sacar(20)


if __name__ == '__main__':
    main()