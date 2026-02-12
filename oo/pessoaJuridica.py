from pessoa import Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, endereco, cnpj):
        super().__init__(nome, telefone, endereco)
        self.cnpj = cnpj

    def exibir_dados(self):
        base = super().exibir_dados()
        return f'Nome Jurídico: {base} \nCNPJ.: {self.cnpj}'
