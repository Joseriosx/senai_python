class Pessoa:

    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def exibir_dados(self):
        return f'{self.nome} \nTelefone: {self.telefone}'