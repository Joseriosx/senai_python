class Produto:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

    def salvar(self):
        linha = f"{self.codigo};{self.descricao};{self.valor}\n"
        with open("produtos.txt", "a", encoding='utf-8') as f:
            f.write(linha)
        print(f"Produto {self.descricao} cadastrado!")   

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'descrição': self.descricao,
            'valor': self.valor
        }