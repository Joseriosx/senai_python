class Endereco:
    def __init__(self, logradouro, bairro, cidade, uf):
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        
    def enderecoCompleto(self):
        return self.logradouro + self.bairro + self.cidade + self.uf