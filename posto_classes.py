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

class NotaFiscal:
    def __init__(self, quantidade, tipo, veiculo, preco):
        self.quantidade = quantidade
        self.tipo = tipo
        self.veiculo = veiculo
        self.preco = preco

    def getQuantidade(self):
        return self.quantidade

    def getTipo(self):
        return self.tipo

    def getVeiculo(self):
        return self.veiculo

    def getPreco(self):
        return self.preco

class Veiculo:
    def __init__(self, tanque):
        self.tanque = tanque

    def abastecer(self, litros, total):

        print('Abastecendo o veículo...')
        self.tanque += litros
        print(f'Abastecimento completo! Preço: R$ {round(total, 2):.2f}  | Total do tanque no tanque do veículo: {round(self.tanque, 2):.2f} litros')

        input('\nDigite algo para retornar ao menu...')
        print('\n '*10)
    
class Limitado(Veiculo):
    def __init__(self, tanque, limite, aceitos):
        super().__init__(tanque)
        self.limite = limite
        self.aceitos = aceitos

    def getAceitos(self):
        return self.aceitos
        

    def abastecer(self, litros, total):
            print('Abastecendo o veículo...')
            self.tanque += litros
            print(f'Abastecimento completo! Preço: R$ {round(total, 2):.2f} | Total no tanque do veículo: {round(self.tanque, 2):.2f} litros')

            input('\nDigite algo para retornar ao menu...')
            print('\n '*10)