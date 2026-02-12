from endereco import Endereco

class Cliente:
    '''   
    def __init__(self, nome, sobrenome, endereco: Endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
    '''

    def __init__(self, nome: str, sobrenome):
        self.nome: str = nome
        self.sobrenome = sobrenome
        self.enderecos: list[Endereco] = []


    def nomeCompleto(self):
        return self.nome + " " + self.sobrenome
    
    def addEndereco(self, endereco: Endereco):
        self.enderecos.append(endereco)

    def visualizarEnderecos(self):
        lista = []
        for endereco in self.enderecos:
            lista.append(endereco.enderecoCompleto())
        return lista