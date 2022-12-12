def caixa_de_texto(string):
    print("\n", "-" * 50, "\n", " " * ((50-len(string))//2),
          string, "\n", "-" * 50, '\n')


def exibir_opcoes(cargo, nome):
    gerente = False
    lista_gerente = ['Lista de combustíveis comercializados', 'Adicionar novo combustível', 'Excluir combustível',
                     'Consultar Faturamento', 'Comprar Combustível', 'Consultar funcionários', 'Abastecer']
    lista_comum = ['Lista de combustíveis comercializados',
                   'Consultar Faturamento', 'Abastecer']
    caixa_de_texto('O melhor Posto do mundo')

    if not (cargo == 'Gerente'):
        lista = lista_comum

    else:
        lista = lista_gerente
        gerente = True

    for i in range(len(lista)):

        print(f'{i+1} - {lista[i]}')
    print('\n ' + f'Logado como: {nome} - {cargo}')

    pick = input(
        '\n ' + 'Digite o número da função que deseja acessar / ou X para voltar ao menu de login: ')

    while (type(pick) != int):

        if (pick.capitalize() == 'X'):
            print('\n ' + 'Voltando para o menu de login...')
            print('\n' * 5)
            break
        
        else:
            try:
                pick = int(pick)
            except:
                print('\n Valor digitado inválido, por favor digite novamente')
                pick = input(' Digite o número da função que deseja acessar: ')

            while not 1 <= pick <= len(lista):
                print('\n Valor digitado inválido, por favor digite novamente')
                pick = input(' Digite o número da função que deseja acessar: ')

    return pick, gerente


def mostra_combustivel(nome_lista, lista, caractere):

    caixa_de_texto(nome_lista)

    if not (len(lista) == 0):

        for x in lista:

            print(f'{caractere}- {x.getNome()}' + ' ' * (10 - len(x.getNome())) +
                  f'|  R$ {round(x.getPreco(), 2):.2f}' + f'  |  {round(x.getEstoque(), 2):.2f} Litros em estoque')

            if (type(caractere) == int):
                caractere += 1

    else:
        print('\nLista vazia')


def mostra_veiculos(lista):

    for i in range(len(lista)):

        print(f'{i+1}- {lista[i]}')


def mostra_extrato(nome_lista, lista):
    faturamento = 0

    caixa_de_texto(nome_lista)
    print()

    for x in lista:
        if x.getPreco() < 0:
            print(' -  R$ {:.2f}'.format(x.getPreco()*-1) + ' ' * (10 - len(str(x.getPreco()))
                                                                   ) + '|   {:.2f} litros de {} adquiridos'.format(x.getQuantidade(), x.getTipo()))
            faturamento = faturamento + x.getPreco()

        if x.getPreco() > 0:
            print(' +  R$ {:.2f}'.format(x.getPreco()) + ' ' * (10 - len(str(x.getPreco()))) +
                  '|   {:.2f} litros de {} abastecidos em "{}"'.format(x.getQuantidade(), x.getTipo(), x.getVeiculo()))
            faturamento = faturamento + x.getPreco()

    print()
    caixa_de_texto('Dinheiro total: R$ {:.2f}'.format(round(faturamento, 2)))


def entrada(tipo, texto, limite, minLimite, maxLimite, cancelavel, completar, completarValor):
    dado = input('\n {}'.format(texto))
    while not (type(dado) == tipo):
        try:
            if cancelavel == 1:
                if dado.capitalize() == 'X':
                    break

            if completar == 1:
                if dado == "Completar":
                    dado = completarValor
                    break

            dado = tipo(dado)

            if limite == 3:
                if not dado >= 0:
                    raise ValueError
                round(dado, 2)
                break

            if limite == 2:
                if not minLimite <= dado <= maxLimite:
                    raise ValueError
                round(dado, 2)
                break

            if limite == 1:
                if not dado > 0:
                    raise ValueError
                round(dado, 2)
                break

            if limite == 0:
                round(dado, 2)
                break
        except:
            print('\n Valor digitado inválido, por favor digite novamente')
            dado = input('\n {}'.format(texto))

    return dado


def login(lista):

    while True:
        incorreto = False

        caixa_de_texto('O melhor Posto do mundo')

        print('Digite os dados para login: ')

        login = input('\nLOGIN: ').lower()

        for x in lista:

            if (x.getLogin() == login):

                senha = input('SENHA: ')

                if (x.getSenha() == senha):

                    print('\nLogin realizado com sucesso!')
                    print('\n' * 3)
                    return x.getNome(), x.getCargo()

                else:
                    print('Senha incorreta! Tente novamente')
                    incorreto = True

        if (not incorreto):

            print('Usuário não cadastrado!')
            print('\n' * 15)
