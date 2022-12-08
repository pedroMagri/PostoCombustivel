class Combustivel:
    def __init__(self, nome, estoque, preco):
        self.nome = nome
        self.estoque = estoque
        self.preco = preco

    def setNome(self, nome):
        self.nome = nome

    def setEstoque(self, estoque):
        self.estoque = estoque

    def setPreco(self, preco):
        self.preco = preco

    def getNome(self):
        return self.nome

    def getEstoque(self):
        return self.estoque

    def getPreco(self):
        return self.preco