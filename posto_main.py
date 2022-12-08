'''
INE5603-01238B
Pedro Henrique Gomes Magri - 22200513
Nicolas Lazzeri Pimenta - 22203241

Sistema de controle de estoque e venda para um posto de combustível (Posto Winterfell)

Informações importantes:
Carros = Todos os carros da cidade possuem um tanque de 50 litros e não é possível colocar outros combustíveis além de Gasolina/Etanol/Diesel
Motos =  Todos as motos da cidade possuem um tanque de 16 litros e não é possível colocar outros combustíveis além de Gasolina/Etanol
Caminhões = Todos os caminhões da cidade possuem um tanque de 300 litros e não é possível colocar outros combustíveis além de Gasolina/Diesel
Outros = Não há limite de tanque e nem restrição ao tipo de combustível

Ações: 
1 - Adicionar/remover/alterar os tipos de combustível vendidos, consultar estoque e tabela de preços
2 - Abastecer e consultar faturamento total

'''


#Imports
import posto_funcionalidades
from posto_Combustivel import Combustivel
from posto_funcoes import exibir_opcoes


#Código Inicial
lista_opcoes = ['Lista de combustíveis comercializados', 'Adicionar novo combustível', 'Excluir combustível', 'Consultar Faturamento', 'Tabela de preços', 'Abastecer']
lista_veiculos = ['Carro', 'Moto', 'Caminhão', 'Outro']
lista_combustiveis = []
c1 = Combustivel('Gasolina', 500, 4.9)
c2 = Combustivel('Etanol', 600, 4.5)
lista_combustiveis.append(c1)
lista_combustiveis.append(c2)



#Código principal
while True:

    exibir_opcoes(lista_opcoes)
    pick = int(input('\nDigite o número da função que deseja acessar: '))

    while not(1 <= pick <= len(lista_opcoes)):
        print('\nValor digitado inválido, por favor digite novamente')
        pick = int(input('Digite o número da função que deseja acessar: '))
        


    if (pick == 1):

        posto_funcionalidades.mostrar_lista_combustiveis(lista_combustiveis)

    elif (pick == 2):

        posto_funcionalidades.adiciona_combustivel(lista_combustiveis)
        
    elif (pick == 3):

        posto_funcionalidades.excluir_combustivel(lista_combustiveis)

    elif (pick == 4):
        print('nao')
    
    elif (pick == 5):

        posto_funcionalidades.tabela_precos(lista_combustiveis)

    elif (pick == 6):

        posto_funcionalidades.abastecimento(lista_veiculos, lista_combustiveis)
        

