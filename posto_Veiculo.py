class Veiculo:
    def __init__(self, tanque):
        self.tanque = tanque

    def abastecer(self, litros, total):

        print('Abastecendo o veículo...')
        self.tanque += litros
        print(f'Abastecimento completo! Total: R$ {total} | {self.tanque} litros')

