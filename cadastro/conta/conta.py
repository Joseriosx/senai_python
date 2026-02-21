from pessoa import Pessoa

class Conta:
    def __init__(self, numero, pessoa: Pessoa):
        self.numero = numero
        self.pessoa = pessoa
        self._saldo = 0

    def visualisarDadosConta(self):
        return f'Número conta: {self.numero} \nTitular: {self.pessoa.nome}'
    
    def visualisarSaldoConta(self):
        return f'Saldo atual: R${self._saldo:.2f}'
    
    def depositar(self, valor):
        self._saldo = self._saldo + valor

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print(f'Saque realizado; Saldo atual da conta: {self._saldo:.2f}')
            return True
        else:
            print('Saldo insuficiente para saque! Verifique o seu saldo e tente novamente.')
            return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            print('Transferencia realizada')
        else:
            print('Transferencia não realizada')
