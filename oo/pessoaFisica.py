from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, endereco, cpf):
        super().__init__(nome, telefone, endereco)
        self.cpf = cpf

    def exibir_dados(self):
        base = super().exibir_dados()
        return f'Nome Físico: {base} \nCPF.: {self.cpf}'
