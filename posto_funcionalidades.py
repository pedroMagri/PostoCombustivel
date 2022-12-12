#Imports
from posto_classes import Combustivel, NotaFiscal, Veiculo, Limitado, Funcionario
from posto_funcoes import mostra_combustivel, caixa_de_texto, mostra_veiculos, mostra_extrato, entrada


#Funções

#1 Lista de combustíveis comercializados
def mostrar_lista_combustiveis(lista, cargo):
    terminar = 0
    print('\n '*10)
    mostra_combustivel('Lista de combustíveis comercializados', lista, 1)

    if not(cargo == 'Gerente'):
        input('\n '*5 + '\nDigite algo para retornar ao menu...')
        print('\n '*10)
        terminar = 1

    else:
        print('\n '*5)
        editar = entrada(int, 'Digite o número do combustível para edita-lo / ou X para retornar ao menu: ', 2, 1, len(lista), 1, 0, 0)

        if str(editar).capitalize() == 'X':
            terminar = 1
            caixa_de_texto('Operação cancelada')

            input('\n '*5 + '\nDigite algo para retornar ao menu...')
            print('\n '*10)

        elif terminar == 0:
            print('\n '*10)
            caixa_de_texto('Editar combustível')

            print(' {}'.format(lista[editar-1].getNome()) + ' ' * (10 - len(lista[editar-1].getNome())) + '  |  R$ {:.2f}'.format(lista[editar-1].getPreco()))

            print('\n 1 - Nome' + '\n 2 - Preço')

            print('\n '*5)
            dado = entrada(int, 'Digite o número correspondente ao dado do combustível para edita-lo / ou X para cancelar a operação: ', 2, 1, 2, 1, 0, 0)

            if str(dado).capitalize() == 'X':
                print('\n '*10)
                caixa_de_texto('Operação cancelada')

                input('\n '*5 + '\nDigite algo para retornar ao menu...')
                print('\n '*10)

            if dado == 1:
                print('\n '*10)
                caixa_de_texto('Editar combustível')

                print(' {}'.format(lista[editar-1].getNome()) + ' ' * (10 - len(lista[editar-1].getNome())) + '  |  R$ {:.2f}'.format(lista[editar-1].getPreco()))

                novoDado = input('\n '*5 + "Digite um novo nome para o combustível / ou X para cancelar: ".format(lista[editar-1].getNome()))

                if novoDado.capitalize() == 'X':
                    print('\n '*10)
                    caixa_de_texto('Operação cancelada')

                    input('\n '*5 + '\nDigite algo para retornar ao menu...')
                    print('\n '*10)

                else:
                    novoDado = novoDado.capitalize()
                    print('\n O nome do combustível "{}" passará a ser "{}"'.format(lista[editar-1].getNome(), novoDado))

                    confirma_ou_nao = str(input('\nDigite S para confirmar / ou N para cancelar:').capitalize())

                    while not (confirma_ou_nao == 'S' or confirma_ou_nao == 'N'):
                        confirma_ou_nao = str(input('Digite S para confirmar / ou N para cancelar:'))

                    if confirma_ou_nao == 'S':
                        lista[editar-1].setNome(novoDado)
                        print('\n '*10)
                        caixa_de_texto('Combustível editado')
                        print(' {}'.format(lista[editar-1].getNome()) + ' ' * (10 - len(lista[editar-1].getNome())) + '  |  R$ {:.2f}'.format(lista[editar-1].getPreco()) + '  |  {:.2f} Litros em estoque'.format(lista[editar-1].getEstoque()))

                        input('\n '*5 + '\nDigite algo para retornar ao menu...')
                        print('\n '*10)

                    else:
                        print('\n '*10)
                        caixa_de_texto('Operação cancelada')

                        input('\n '*5 + '\nDigite algo para retornar ao menu...')
                        print('\n '*10)

            if dado == 2:
                print('\n '*10)
                caixa_de_texto('Editar combustível')

                print(' {}'.format(lista[editar-1].getNome()) + ' ' * (10 - len(lista[editar-1].getNome())) + '  |  R$ {:.2f}'.format(lista[editar-1].getPreco()))

                print('\n '*5)
                novoDado = entrada(float, 'Digite um novo preço para o combustível do tipo {} / ou X para cancelar: '.format(lista[editar-1].getNome()), 1, 0, 0, 1, 0, 0)

                if type(novoDado) == str:
                    if novoDado.capitalize() == 'X':
                        print('\n '*10)
                        caixa_de_texto('Operação cancelada')

                        input('\n '*5 + '\nDigite algo para retornar ao menu...')
                        print('\n '*10)

                else:

                    print('\n O preço do combustível do tipo "{}" passará a ser R$ {:.2f}'.format(lista[editar-1].getNome(), novoDado))

                    confirma_ou_nao = str(input('\nDigite S para confirmar / ou N para cancelar:').capitalize())

                    while not (confirma_ou_nao == 'S' or confirma_ou_nao == 'N'):
                        confirma_ou_nao = str(input('Digite S para confirmar / ou N para cancelar:'))

                    if confirma_ou_nao == 'S':
                        lista[editar-1].setPreco(novoDado)
                        print('\n '*10)
                        caixa_de_texto('Combustível editado')
                        print(' {}'.format(lista[editar-1].getNome()) + ' ' * (10 - len(lista[editar-1].getNome())) + '  |  R$ {:.2f}'.format(lista[editar-1].getPreco()) + '  |  {:.2f} Litros em estoque'.format(lista[editar-1].getEstoque()))

                        input('\n '*5 + '\nDigite algo para retornar ao menu...')
                        print('\n '*10)

                    else:
                        print('\n '*10)
                        caixa_de_texto('Operação cancelada')

                        input('\n '*5 + '\nDigite algo para retornar ao menu...')
                        print('\n '*10)
    


#2 Adicionar novo combustível
def adiciona_combustivel(lista):
    termina = 0
    print('\n '*10)
    caixa_de_texto('Adicionar novo combustível')

    print(' - Combustível' + ' ' * (10 - len('Combustível')) + '  |  R$ 00.00' + '  |  00.00 Litros em estoque')

    nome = input('\n '*5 + "Digite o nome do combustível que deseja adicionar / ou digite X para cancelar: ").capitalize()

    for d in lista:
        if nome == d.getNome():
            termina = 1
            print('\n '*10)

            caixa_de_texto('Operação cancelada')
            print('\n O combustível do tipo "{}" já está cadastrado'.format(nome))
            print('\n Para edita-lo acesse "Lista de combustíveis comercializados" no menu')

            input('\n '*5 + '\nDigite algo para retornar ao menu...')
            print('\n '*10)


    if (nome == 'X'):
        print('\n '*10)
        caixa_de_texto('Operação cancelada')

        input('\n '*5 + '\nDigite algo para retornar ao menu...')
        print('\n '*10)

    elif termina == 0:

        print('\n '*10)
        caixa_de_texto('Adicionar novo combustível')
        print(' - {}'.format(nome) + ' ' * (10 - len(nome)) + '|  R$ 00.00' + '  |  00.00 Litros em estoque')

        print('\n '*5)
        preco = entrada(float, 'Digite o preço que o novo combustível será vendido: ', 1, 0, 0, 0, 0, 0)

        print('\n '*10)
        caixa_de_texto('Adicionar novo combustível')
        print(' - {}'.format(nome) + ' ' * (10 - len(nome)) + '|  R$ {:.2f}'.format(preco) + '  |  00.00 Litros em estoque')

        print('\n '*5)
        estoque = entrada(float, 'Digite a quantidade de litros no estoque: ', 3, 0, 0, 0, 0, 0)

        print('\n '*10)
        caixa_de_texto('Combustível adicionado')
        print(' - {}'.format(nome) + ' ' * (10 - len(nome)) + '|  R$ {:.2f}'.format(preco) + '  |  {:.2f} Litros em estoque'.format(estoque))

        input('\n '*5 + '\nDigite algo para retornar ao menu...')
        print('\n '*10)

        novo = Combustivel(nome, estoque, preco)

        lista.append(novo)


#3 Excluir combustível
def excluir_combustivel(lista):
    print('\n '*10)
    mostra_combustivel('Excluir combustível', lista, 1)

    print('\n '*5)
    excluir = entrada(int, 'Digite o número do combustível que deseja excluir: ', 2, 1, len(lista), 0, 0, 0)


    print('\n O combustível do tipo {} será excluído permanentemente, deseja continuar? '.format(lista[excluir-1].getNome()))

    confirma_ou_nao = str(input('\n Digite S para confirmar a exclusão / ou N para cancelar:').capitalize())
    while not (confirma_ou_nao == 'S' or confirma_ou_nao == 'N'):
        confirma_ou_nao = str(input(' Digite S para confirmar a exclusão / ou N para cancelar:'))

    if confirma_ou_nao == 'S':
        lista.pop(excluir-1)
        print('\n '*10)
        caixa_de_texto('Combustível excluído')
        input('\n '*5 + '\nDigite algo para retornar ao menu...')
        print('\n '*10)

    else:

        print('\n '*10)
        caixa_de_texto('Operação cancelada'.format(lista[excluir-1].getNome()))
        input('\n '*5 + '\nDigite algo para retornar ao menu...')
        print('\n '*10)


#4 Consultar Faturamento
def mostrar_faturamento(lista):
    print('\n '*10)
    mostra_extrato('Faturamento', lista)

    input('\n '*5 + 'Digite algo para retornar ao menu...')
    print('\n '*10)


#5 Comprar Combustível
def comprar_combustivel(lista, lista2):
    print('\n '*10)
    lucro = 30
    cont = 1

    print('\n '*10)
    caixa_de_texto('Compra de Combustível')

    print('')
    # lucro = int(input("\nDigite a margem de lucro que deseja: "))
    for i in lista:
            
        print(f'{cont} - {i.getNome()}' + ' ' * (10 - len(i.getNome())) + f'|  R$ {round(i.getPreco()*((100-lucro)/100), 2):.2f} por litro')
        cont += 1

    print('\n '*5)
    comprar = entrada(int, 'Digite o número do combustível que deseja comprar: ', 2, 1, cont, 0, 0, 0)


    print('\n '*5)
    qtd_comprando = entrada(float, 'Digite quantos litros de {} que deseja comprar: '.format(lista[comprar-1].getNome()), 3, 0, 0, 0, 0, 0)

    print('\n '*5 + 'Adquirindo {:.2f} litros de {} você gastará R$ {:.2f}'.format(qtd_comprando, lista[comprar-1].getNome(), round(lista[comprar-1].getPreco()*((100-lucro)/100), 2)*qtd_comprando))
    confirma_ou_nao = str(input('\n Digite S para confirmar a compra / ou N para cancelar:').capitalize())

    while not (confirma_ou_nao == 'S' or confirma_ou_nao == 'N'):
        confirma_ou_nao = str(input(' Digite S para confirmar a compra / ou N para cancelar:'))
    
    if confirma_ou_nao == 'S':
        print('\n '*10)
        caixa_de_texto(' {:.2f} litros de {} adquiridos por R$ {:.2f}'.format(qtd_comprando, lista[comprar-1].getNome(), round(lista[comprar-1].getPreco()*((100-lucro)/100), 2)*qtd_comprando))

        lista[comprar-1].setEstoque(lista[comprar-1].getEstoque()+qtd_comprando)

        compra = NotaFiscal(qtd_comprando, lista[comprar-1].getNome(), 'nenhum', (round(lista[comprar-1].getPreco()*((100-lucro)/100), 2)*qtd_comprando*-1))

        lista2.append(compra)

        input('\n '*5 + 'Digite algo para retornar ao menu...')
        print('\n '*10)

    if confirma_ou_nao == 'N':
        print('\n '*10)
        caixa_de_texto('Compra cancelada')

        input('\n '*5 + 'Digite algo para retornar ao menu...')
        print('\n '*10)


#6 Abastecer
def abastecimento(lista1, lista2, lista3):
    outro = False
    print('\n '*10)
    caixa_de_texto('Abastecimento')
    estoque_combustiveis = list()

    mostra_veiculos(lista1)

    print('\n '*5)
    escolha = entrada(int, 'Digite o número correspondente ao tipo de veículo que deseja abastecer: ', 2, 1, len(lista1), 0, 0, 0)

    if escolha == 1:
        print('\n '*10)
        caixa_de_texto('Abastecendo "Carro"')
        print()
        print('''                                 _________
                          _.--""'-----,   `"--.._
                       .-''   _/_      ; .'"----,`-,
                     .'      :___:     ; :      ;;`.`.
                    .      _.- _.-    .' :      ::  `..
                 __;..----------------' :: ___  ::   ;;
            .--"". '           ___.....`:=(___)-' :--'`.
          .'   .'         .--''__       :       ==:    ;
      .--/    /        .'.''     ``-,   :         :   '`-.__
   ."', :    /       .'-`\ \       .--.\ :         :  ,   _ \ 
  ;   ; |   ;       /:'  ;;      /__  \ \:         :  :  /_\ \ 
  |\_/  |   |      / \__//      /"--\ \ \:         :  : ;|`\ |    
  : "  /\__/\____//   """      /     \ \ :         :  : :|'| |
["""""""""--------........._  /      | | ;      __.:--' :|// |
 "------....______         ].'|      / / |--"""'__...-'`\ \/ /
   `| POO2022 |__;_...--'": :  \    / /  |---"""      \__\__/
     """""""""'            \ \  \_./ / ./
       `---'                \ \_     _/
                             `--`---'   ''')

        print('\n '*2)
        tanque = entrada(float, 'Digite a quantidade de litros atualmente no tanque (Capacidade máxima do tanque -> 50 litros): ', 2, 0, 50, 0, 0, 0)

        v1 = Limitado(tanque, 50, ['Gasolina', 'Etanol', 'Diesel'])
        veiculo = 'Carro'

    if escolha == 2:
        print('\n '*10)
        caixa_de_texto('Abastecendo "Moto"')
        print()
        print('''                                    ,-~ |
       ________________          o==]___|
      |                |            \ \ 
      |________________|            /\ \ 
 __  /  _,-----._      )           |  \ \.
|_||/_-~         `.   /()          |  /|]_|_____
  |//              \ |              \/ /_-~     ~-_
  //________________||              / //___________\ 
 //__|______________| \____________/ //___/-\ \~-_
((_________________/_-o___________/_//___/  /\,\  \ 
 |__/(  ((====)o===--~~                 (  ( (o/)  )
      \  ``==' /                         \  `--'  /
       `-.__,-'                           `-.__,-' ''')

        print('\n '*2)
        tanque = entrada(float, 'Digite a quantidade de litros atualmente no tanque (Capacidade máxima do tanque -> 16 litros): ', 2, 0, 16, 0, 0, 0)

        v1 = Limitado(tanque, 16, ['Gasolina', 'Etanol'])
        veiculo = 'Moto'

    if escolha == 3:
        print('\n '*10)
        caixa_de_texto('Abastecendo "Caminhão"')
        print()
        print('''                       _____________________________________________________
                      |                                                     |
             _______  |                                                     |
            / _____ | |                                                     |
           / /(__) || |                                                     |
  ________/ / |OO| || |                                                     |
 |         |-------|| |                                                     |
(|         |     -.|| |_______________________                              |
 |  ____   \       ||_________||____________  |             ____      ____  |
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |\ 
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |
    \__/                   \__/     \__/                    \__/      \__/                                 ''')

        print('\n '*2)
        tanque = entrada(float, 'Digite a quantidade de litros atualmente no tanque (Capacidade máxima do tanque -> 300 litros): ', 2, 0, 300, 0, 0, 0)

        v1 = Limitado(tanque, 300, ['Gasolina', 'Diesel'])
        veiculo = 'Caminhão'

    if (escolha == 4):
        outro = True
        caixa_de_texto('Abastecendo "Outro"')
        print()


        print('\n '*5)
        tanque = entrada(float, 'Digite a quantidade de litros atualmente no tanque: ', 1, 0, 0, 0, 0, 0)

                
        v1 = Veiculo(tanque)
        cont = 1
        print('\n '*10)
        caixa_de_texto('Abastecendo "Outro"')
        print()

        for i in lista2:

                print(f'{cont} - {i.getNome()}' + ' ' * (10 - len(i.getNome())) + f'|  R$ {round(i.getPreco(), 2):.2f} por litro')
                combustivel = i.getEstoque(), i.getPreco(), i.getNome()
                estoque_combustiveis.append(combustivel)
                cont += 1

        print('\n '*5)
        escolha = entrada(int, 'Digite o número do combustível que deseja utilizar: ', 1, 1, len(lista2), 0, 0, 0)

        caixa_de_texto('Abastecendo "Outro"')
        print()

        print(' {}'.format(estoque_combustiveis[escolha-1][2]) + ' ' * (10 - len(estoque_combustiveis[escolha-1][2])) + '  |  R$ {:.2f}'.format(estoque_combustiveis[escolha-1][1]) + '  |  {:.2f} Litros em estoque'.format(estoque_combustiveis[escolha-1][0]))

        print('\n '*5)
        qtd_abastecendo = entrada(float, 'Digite quantos litros de {} deseja abastecer: '.format(estoque_combustiveis[escolha-1][2]), 0, 0, 0, 0, 0, 0)

        if qtd_abastecendo > estoque_combustiveis[escolha-1][0]:
            print('\n '*5 + 'Não há estoque o suficiente para abastecer essa quantidade')
            print('\n Estoque Disponível: {:.2f} litros de {}'.format(estoque_combustiveis[escolha-1][0], estoque_combustiveis[escolha-1][2]))
            
        else:
            v1.abastecer(qtd_abastecendo, qtd_abastecendo*estoque_combustiveis[escolha-1][1])

            for j in range(0, len(lista2)):
                if lista2[j].getNome() == estoque_combustiveis[escolha-1][2]:
                    lista2[j].setEstoque(lista2[j].getEstoque()-qtd_abastecendo)

                    venda = NotaFiscal(qtd_abastecendo, lista2[j].getNome(), 'Outro', (round(lista2[j].getPreco(), 2)*qtd_abastecendo))
                    lista3.append(venda)
    
    if not(escolha == 4) and (not outro):

        if tanque == v1.limite:
            print('\n '*10)
            caixa_de_texto('Operação cancelada')
            print('\n O tanque do veículo já está cheio')
            input('\n '*5 + 'Digite algo para retornar ao menu...')
            print('\n '*10)

        else:
            
            cont = 1
            caixa_de_texto('Abastecendo "{}"'.format(veiculo))
            print()
            for x in v1.getAceitos():

                for i in lista2:

                    if (x == i.getNome()):
                        print(f'{cont} - {x}' + ' ' * (10 - len(x)) + f'|  R$ {round(i.getPreco(), 2):.2f} por litro')
                        combustivel = i.getEstoque(), i.getPreco(), i.getNome()
                        estoque_combustiveis.append(combustivel)
                        cont += 1
            print('\n '*5)

            escolha = entrada(int, 'Digite o número do combustível que deseja utilizar: ', 1, 1, len(estoque_combustiveis), 0, 0, 0)

            caixa_de_texto('Abastecendo "{}"'.format(veiculo))
            print()

            print(' {}'.format(estoque_combustiveis[escolha-1][2]) + ' ' * (10 - len(estoque_combustiveis[escolha-1][2])) + '  |  R$ {:.2f}'.format(estoque_combustiveis[escolha-1][1]) + '  |  {:.2f} Litros em estoque'.format(estoque_combustiveis[escolha-1][0]))

            qtd_abastecendo = entrada(float, 'Digite quantos litros de {} deseja abastecer / ou escreva "completar" para encher o tanque: '.format(estoque_combustiveis[escolha-1][2]).capitalize(), 1, 0, 0, 0, 1, v1.limite-v1.tanque) 

            while not v1.limite >= qtd_abastecendo + v1.tanque:
                qtd_abastecendo = entrada(float, '\n Valor digitado ultrapassou o limite de {:.2f} litros do tanque, digite outro ou "Completar": '.format(v1.limite).capitalize(), 1, 0, 0, 0, 1, v1.limite-v1.tanque) 


            if qtd_abastecendo > estoque_combustiveis[escolha-1][0]:
                print('\n '*10)
                caixa_de_texto('Operação cancelada')
                print('\n '*2 + 'Estoque Disponível: {:.2f} litros de {}'.format(estoque_combustiveis[escolha-1][0], estoque_combustiveis[escolha-1][2]))
                print('\n Não há estoque o suficiente para abastecer essa quantidade')

                input('\n '*5 + 'Digite algo para retornar ao menu...')
                print('\n '*10)
                
                
            else:
                v1.abastecer(qtd_abastecendo, qtd_abastecendo*estoque_combustiveis[escolha-1][1])

                for j in range(0, len(lista2)):
                    if lista2[j].getNome() == estoque_combustiveis[escolha-1][2]:
                        lista2[j].setEstoque(lista2[j].getEstoque()-qtd_abastecendo)

                        venda = NotaFiscal(qtd_abastecendo, lista2[j].getNome(), veiculo, (round(lista2[j].getPreco(), 2)*qtd_abastecendo))
                        lista3.append(venda)

def consultar_funcionarios(lista, caractere):
    print('\n' * 5)
    caixa_de_texto('Funcionários')

    if not(len(lista) == 0):

        for x in lista:

            print(f'{caractere}- {x.getNome()}' + ' ' * (10 - len(x.getNome())) + f'|   {x.getCargo()}' + ' ' * (15 - len(x.getCargo())) + f'|  {x.getCpf()}')

            if (type(caractere) == int):
                caractere += 1

        opcao = input('\n' * 5 + 'Digite "A" se deseja adicionar um funcionário, "E" para excluir um funcionário ou "X" para retornar ao menu: ').capitalize()

        while (opcao != 'A') and (opcao != 'E') and (opcao != 'X'):
            print('\n Valor digitado inválido, por favor digite novamente')
            opcao = input(' Digite o número da função que deseja acessar: ')

        if (opcao == 'X'):
            print('\n ' + 'Voltando para o menu de login...')
            print('\n' * 5)

        if (opcao == 'A'):
            print('\n' * 5)
            caixa_de_texto('Adicionando novo funcionário')

            nome = input('Digite o nome do novo funcionário: ').capitalize()
            cargo = input('Digite o cargo do novo funcionário: ').capitalize()
            cpf = input('Digite o CPF do novo funcionário: ')
            login = input('Digite o login do novo funcionário: ')
            senha = input('Digite a senha do novo funcionário: ')
            func = Funcionario(nome, cpf, cargo, login, senha)
            lista.append(func)
        
        if (opcao == 'E'):
            print('\n ')
            excluir = entrada(int, 'Digite o número do funcionário que deseja excluir: ', 2, 1, len(lista), 0, 0, 0)


            print(f'\n O funcionário "{lista[excluir-1].getNome()}" será excluído permanentemente, deseja continuar? ')

            confirma_ou_nao = str(input('\n Digite S para confirmar a exclusão / ou N para cancelar: ').capitalize())
            while not (confirma_ou_nao == 'S' or confirma_ou_nao == 'N'):
                confirma_ou_nao = str(input(' Digite S para confirmar a exclusão / ou N para cancelar: '))

            if confirma_ou_nao == 'S':
                lista.pop(excluir-1)
                print('\n '*10)
                caixa_de_texto('Funcionário excluído')
                input('\n '*5 + '\nDigite algo para retornar ao menu...')
                print('\n '*10)

            else:

                print('\n '*10)
                caixa_de_texto('Operação cancelada'.format(lista[excluir-1].getNome()))
                input('\n '*5 + '\nDigite algo para retornar ao menu...')
                print('\n '*10)

    else:
        print('\nLista de funcionários vazia')

