class Cliente:

    def __init__(self, cpf, nomeCompleto):
        self.cpf = cpf
        self.nomeCompleto = nomeCompleto

    def salvar(self):
        linha = f'{self.nomeCompleto}; {self.cpf}\n'
        with open('clientes.txt', 'a', encoding='utf-8') as f:
            f.write(linha)
        print(f'Cliente {self.nomeCompleto} cadastrado!\n')
        

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nomeCompleto
        }