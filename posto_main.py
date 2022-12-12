'''
INE5603-01238B
Pedro Henrique Gomes Magri - 22200513
Nicolas Lazzeri Pimenta - 22203241

'''


#Imports
import posto_funcionalidades
from posto_classes import Combustivel, Funcionario
from posto_funcoes import exibir_opcoes, caixa_de_texto, login


#Código Inicial
lista_veiculos = ['Carro', 'Moto', 'Caminhão', 'Outro']
lista_combustiveis = [Combustivel('Gasolina', 500, 4.90), Combustivel('Etanol', 600, 4.50), Combustivel('Diesel', 1500, 3.70)]
lista_funcionarios = [Funcionario('Pimenta', '039.105.965.21', 'Gerente', 'pimenta123', '2503'), Funcionario('Magri', '029.320.560-70', 'Frentista', 'magri123', 'didico13')]
lista_faturamento = []


#Código principal
while True:

    nome, cargo = login(lista_funcionarios)

    while True:

        pick, gerente = exibir_opcoes(cargo, nome)

        if (pick == 1):
            posto_funcionalidades.mostrar_lista_combustiveis(lista_combustiveis, cargo)

        if (pick == 2):

            if (gerente):
                posto_funcionalidades.adiciona_combustivel(lista_combustiveis)
            
            else:
                posto_funcionalidades.mostrar_faturamento(lista_faturamento)
            
        if (pick == 3):

            if (gerente):
                posto_funcionalidades.excluir_combustivel(lista_combustiveis)
            
            else:
                if not len(lista_combustiveis):
                    caixa_de_texto('Operação cancelada')
                    print('\n Não há nenhum combustível para abastecer um veículo')
                else:
                    posto_funcionalidades.abastecimento(lista_veiculos, lista_combustiveis, lista_faturamento)
                
        if (pick == 4) and gerente:
            posto_funcionalidades.mostrar_faturamento(lista_faturamento)

        if (pick == 5) and gerente:
            posto_funcionalidades.comprar_combustivel(lista_combustiveis, lista_faturamento)

        if (pick == 6):

            posto_funcionalidades.consultar_funcionarios(lista_funcionarios, 1)

        if (pick == 7) and gerente:
            if not len(lista_combustiveis):
                caixa_de_texto('Operação cancelada')
                print('\n Não há nenhum combustível para abastecer um veículo')
            else:
                posto_funcionalidades.abastecimento(lista_veiculos, lista_combustiveis, lista_faturamento)

        if (type(pick) == str):
            if (pick.capitalize() == 'X'):
                break
