from posto_Veiculo import Veiculo

class Limitado(Veiculo):
    def __init__(self, tanque, limite, aceitos):
        super().__init__(tanque)
        self.limite = limite
        self.aceitos = aceitos

    def getAceitos(self):
        return self.aceitos
        

    def abastecer(self, litros, total):
        
        if (self.limite >= litros + self.tanque):

            print('Abastecendo o veículo...')
            self.tanque += litros
            print(f'Abastecimento completo! Total: R$ {total} | {self.tanque} litros')

        else:

            print('Não foi possível abastecer o seu veículo, o valor digitado ultrapassou o limite do tanque')