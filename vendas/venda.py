import json

class Venda:
    def __init__(self, codigo, cliente):
        self.codigo = codigo
        self.cliente = cliente
        self._produtos = []

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'cliente': self.cliente.to_dict(),
            'produtos': [p.to_dict() for p in self._produtos],
            'total': self._total
        }

    def salvar(self):
        with open('vendas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(self.to_dict(), arquivo, indent=4)

    def addProdutoVenda(self, produto):
        self._produtos .append(produto)

    def total(self):
        acumulador = 0
        for p in self._produtos:
            acumulador += p.valor