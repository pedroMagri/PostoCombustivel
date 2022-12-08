#Imports
from posto_VeiculoComLimite import Limitado
from posto_Veiculo import Veiculo
from posto_Combustivel import Combustivel
from posto_funcoes import mostra_combustivel, caixa_de_texto, mostra_veiculos


#Funções

#1
def mostrar_lista_combustiveis(lista):

    mostra_combustivel('Lista de combustíveis comercializados', lista, '')

#2
def adiciona_combustivel(lista):

    caixa_de_texto('Adicionar novo combustível')

    nome = input("Digite o nome do combústivel que deseja adicionar / ou digite N para cancelar: ").capitalize()
        
    if not(nome == 'N'):
        estoque = int(input("Digite a quantidade de litros no estoque: "))
        preco = float(input("Digite o preço que o novo combustível será vendido: "))

        novo = Combustivel(nome, estoque, preco)

        lista.append(novo)

#3
def excluir_combustivel(lista):

    mostra_combustivel('Excluir combustível', lista, 1)

    excluir = int(input("\nDigite o número do combustível que deseja excluir: "))

    lista.pop(excluir-1)

#4




#5
def tabela_precos(lista):

    mostra_combustivel('Tabela de preços', lista, '')

#6
def abastecimento(lista1, lista2):

    caixa_de_texto('Abastecimento')

    mostra_veiculos(lista1)

    escolha = int(input('\nDigite o número correspondente ao tipo de veículo que deseja abastecer: '))
    
    tanque = int(input('Digite a quantidade de litros atualmente no tanque: '))

    if (escolha == 1):

        v1 = Limitado(tanque, 50, ['Gasolina', 'Etanol', 'Diesel'])

    if (escolha == 2):

        v1 = Limitado(tanque, 16, ['Gasolina', 'Etanol'])

    if (escolha == 3):

        v1 = Limitado(tanque, 300, ['Gasolina', 'Diesel'])

    if (escolha == 4):

        v1 = Veiculo(tanque)
    
    cont = 1
    print()
    for x in v1.getAceitos():

        for i in lista2:

            if (x == i.getNome()):
                
                print(f'{cont}- {x}' + ' ' * (10 - len(x)) + f'|  {i.getPreco()}')
                cont += 1

    escolha = int(input("\nDigite o número do combustível que deseja utilizar: "))





