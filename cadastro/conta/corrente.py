from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, pessoa):
        super().__init__(numero, pessoa)
        self.limite = 500

    def sacar(self, valor):
        total = self._saldo + self.limite
        if total >= valor:
            self._saldo -= valor
            return True
        else:
            print('Saldo insuficiente para saque! Verifique o seu saldo e tente novamente.')
            return False

        