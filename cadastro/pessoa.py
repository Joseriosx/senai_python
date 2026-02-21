class Pessoa:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        return f'{self.nome} \nTelefone: {self.telefone}'