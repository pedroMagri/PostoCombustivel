from posto_funcoes_formatacao import caixa_de_texto

def exibir_opcoes(opcoes):

    caixa_de_texto('Posto Winterfell')
    
    for i in range(len(opcoes)):

        print(f'{i+1} - {opcoes[i]}')


def mostra_combustivel(nome_lista, lista, caractere):

    caixa_de_texto(nome_lista)

    if not(len(lista) == 0):
        
        if not(nome_lista == 'Tabela de preços'):
            for x in lista:

                print(f'{caractere}- {x.getNome()}' + ' ' * (10 - len(x.getNome())) + f'|  {x.getEstoque()}')
                
                if (type(caractere) == int):

                    caractere += 1

        else:

            for x in lista:

                print(f'{caractere}- {x.getNome()}' + ' ' * (10 - len(x.getNome())) + f'|  {x.getPreco()}')
                
                if (type(caractere) == int):

                    caractere += 1

    else:
        print('\nLista vazia')


def mostra_veiculos(lista):

    for i in range(len(lista)):

        print(f'{i+1}- {lista[i]}')


