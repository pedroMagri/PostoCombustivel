'''
INE5603-01238B
Pedro Henrique Gomes Magri - 22200513
Nicolas Lazzeri Pimenta - 22203241

'''


#Imports
import posto_funcionalidades
from posto_classes import Combustivel
from posto_funcoes import exibir_opcoes, caixa_de_texto


#Código Inicial
lista_opcoes = ['Lista de combustíveis comercializados', 'Adicionar novo combustível', 'Excluir combustível', 'Consultar Faturamento', 'Comprar Combustível', 'Abastecer']
lista_veiculos = ['Carro', 'Moto', 'Caminhão', 'Outro']
lista_combustiveis = [Combustivel('Gasolina', 500, 4.90), Combustivel('Etanol', 600, 4.50), Combustivel('Diesel', 1500, 3.70)]
lista_faturamento = list()



#Código principal
while True:

    exibir_opcoes(lista_opcoes)
    print('\n ' + 'Logado como: GERENTE')
    pick = input('\n ' + 'Digite o número da função que deseja acessar: ')

    while not(type(pick) == int):
        try:
            pick = int(pick)
        except:
            print('\n Valor digitado inválido, por favor digite novamente')
            pick = input(' Digite o número da função que deseja acessar: ')

    while not 1 <= pick <= len(lista_opcoes):
            print('\n Valor digitado inválido, por favor digite novamente')
            pick = input(' Digite o número da função que deseja acessar: ')


        


    if (pick == 1):
        posto_funcionalidades.mostrar_lista_combustiveis(lista_combustiveis)

    if (pick == 2): ## SÓ GERENTE
        posto_funcionalidades.adiciona_combustivel(lista_combustiveis)
        
    if (pick == 3): ## SÓ GERENTE
        posto_funcionalidades.excluir_combustivel(lista_combustiveis)

    if (pick == 4):
        posto_funcionalidades.mostrar_faturamento(lista_faturamento)

    if (pick == 5): ## SÓ GERENTE
        posto_funcionalidades.comprar_combustivel(lista_combustiveis, lista_faturamento)

    if (pick == 6):
        if len(lista_combustiveis) == 0:
            caixa_de_texto('Operação cancelada')
            print('\n Não há nenhum combustível para abastecer um veículo')
        else:
            posto_funcionalidades.abastecimento(lista_veiculos, lista_combustiveis, lista_faturamento)
        

